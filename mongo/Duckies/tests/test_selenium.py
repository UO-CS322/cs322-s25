import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import sys
import threading
from requests.exceptions import ConnectionError

# Add the project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from .selenium_config import (
    DuckApp,
    find_free_port,
    wait_for_flask_server,
    cleanup_flask,
    flask_thread,
)


@pytest.fixture(scope="module")
def web_driver():
    """Create a Chrome WebDriver instance"""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
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


def test_add_duck(web_driver, flask_app):  # type: ignore
    """Test adding a duck to the database"""
    # Navigate to the application
    web_driver.get(f"http://localhost:{flask_app.test_port}")

    # Wait for the page to load
    WebDriverWait(web_driver, 1).until(
        EC.presence_of_element_located((By.ID, "duckName"))
    )

    # Fill in the form
    web_driver.find_element(By.ID, "duckName").send_keys("Test Duck")
    web_driver.find_element(By.ID, "duckType").send_keys("Rubber")
    web_driver.find_element(By.ID, "duckValue").send_keys("10")

    # Click the add button
    web_driver.find_element(By.ID, "addDuckButton").click()

    # Wait for success message
    WebDriverWait(web_driver, 1).until(
        EC.text_to_be_present_in_element(
            (By.ID, "addResult"), "Duck added successfully"
        )
    )

    # Verify the success message
    result = web_driver.find_element(By.ID, "addResult").text
    assert "Duck added successfully" in result


def test_search_duck(web_driver, flask_app):  # type: ignore
    """Test searching for a duck in the database"""
    # Navigate to the application
    web_driver.get(f"http://localhost:{flask_app.test_port}")

    # Wait for the page to load
    WebDriverWait(web_driver, 1).until(
        EC.presence_of_element_located((By.ID, "searchName"))
    )

    # Fill in the search form
    web_driver.find_element(By.ID, "searchName").send_keys("Test Duck")
    web_driver.find_element(By.ID, "duckType").send_keys("Rubber")
    web_driver.find_element(By.ID, "duckValue").send_keys("10")

    # Click the search button
    web_driver.find_element(By.ID, "searchDuckButton").click()

    # Wait for search results
    WebDriverWait(web_driver, 1).until(
        EC.text_to_be_present_in_element((By.ID, "searchResult"), "Test Duck")
    )

    # Verify the search results
    result = web_driver.find_element(By.ID, "searchResult").text
    assert "Test Duck" in result
    assert "Rubber" in result
    assert "10" in result
