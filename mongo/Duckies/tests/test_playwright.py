import pytest
from playwright.sync_api import Page, expect
import os
import sys
import threading
import time
import requests
from requests.exceptions import ConnectionError

# Add the project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from app import DuckApp

# Global variable to store the Flask thread
flask_thread = None


def find_free_port():
    """Find a free port to use"""
    import socket

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        return s.getsockname()[1]


def wait_for_flask_server(port, timeout=10):
    """Wait for Flask server to be ready"""
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            response = requests.get(f"http://localhost:{port}")
            if response.status_code == 200:
                return True
        except ConnectionError:
            time.sleep(0.1)
    return False


def cleanup_flask():
    """Clean up Flask thread on exit"""
    global flask_thread
    if flask_thread and flask_thread.is_alive():
        flask_thread.join(timeout=5)


@pytest.fixture(scope="session")
def flask_app():
    """Create and run the Flask application in a separate thread"""
    global flask_thread

    # Find a free port
    test_port = find_free_port()

    app = DuckApp(test_mode=True)

    def run_app():
        app.run(port=test_port, debug=False)

    # Start Flask in a separate thread
    flask_thread = threading.Thread(target=run_app)
    flask_thread.daemon = True
    flask_thread.start()

    # Wait for the server to be ready
    if not wait_for_flask_server(test_port):
        raise RuntimeError("Flask server failed to start within the timeout period")

    # Store the port in the app object for tests to access
    app.test_port = test_port

    yield app

    # Cleanup
    if flask_thread and flask_thread.is_alive():
        flask_thread.join(timeout=5)


@pytest.fixture(scope="session")
def base_url(flask_app):
    """Get the base URL for the Flask app"""
    return f"http://localhost:{flask_app.test_port}"


def test_add_duck(page: Page, base_url):
    """Test adding a duck through the web interface"""
    # Go to the home page
    page.goto(base_url)

    # Fill in the duck details
    page.fill("#duckName", "Test Duck")
    page.fill("#duckType", "Rubber")
    page.fill("#duckValue", "10")

    # Click the add button
    page.click("#addDuckButton")

    # Wait for success message
    expect(page.locator("#addResult")).to_contain_text("Duck added successfully")


def test_find_duck(page: Page, base_url):
    """Test finding a duck through the web interface"""
    # Go to the home page
    page.goto(base_url)

    # Search for the duck we just added
    page.fill("#searchName", "Test Duck")
    page.click("#searchDuckButton")

    # Wait for and verify search results
    result = page.locator("#searchResult")
    expect(result).to_contain_text("Test Duck")
    expect(result).to_contain_text("Rubber")
    expect(result).to_contain_text("10")


def test_clear_search(page: Page, base_url):
    """Test clearing the search results"""
    # Go to the home page
    page.goto(base_url)

    # Search for a duck
    page.fill("#searchName", "Test Duck")
    page.click("#searchDuckButton")

    # Clear the search
    page.click("#clearSearch")

    # Verify search results are cleared
    expect(page.locator("#searchResult")).to_be_empty()
