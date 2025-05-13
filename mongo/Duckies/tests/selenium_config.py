import os
import sys
import time
import atexit
import requests
from requests.exceptions import ConnectionError
import socket

# Add the project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from app import DuckApp  # type: ignore

# Global variable to store the Flask thread
flask_thread = None


def find_free_port():
    """Find a free port to use"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        return s.getsockname()[1]


def wait_for_flask_server(server_port, max_retries=30, retry_interval=1):
    """Wait for the Flask server to be ready to accept connections"""
    for _ in range(max_retries):
        try:
            response = requests.get(f"http://localhost:{server_port}", timeout=1)
            if response.status_code == 200:
                return True
        except (ConnectionError, requests.exceptions.Timeout):
            time.sleep(retry_interval)
    return False


def cleanup_flask():
    """Cleanup function to be called when the program exits"""
    global flask_thread
    if flask_thread and flask_thread.is_alive():
        flask_thread.join(timeout=5)


# Register the cleanup function
atexit.register(cleanup_flask)
