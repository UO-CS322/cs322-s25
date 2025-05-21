import pytest
from pymongo import MongoClient
import os
import sys

# Add the project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from app import DuckApp


# Test client
@pytest.fixture(name="test_client")
def client_fixture():
    app = DuckApp(test_mode=True)
    app.app.config["TESTING"] = True
    with app.app.test_client() as client:
        yield client


# Test database
@pytest.fixture(name="test_db")
def db_fixture():
    # Connect to test database
    mongo_client = MongoClient("localhost", 27017)
    db = mongo_client["test_duckdb"]
    collection = db["test_ducks"]

    # Clear the collection before each test
    collection.delete_many({})

    yield collection

    # Clean up after tests
    collection.delete_many({})
    mongo_client.drop_database("test_duckdb")


def test_home_page(test_client):
    """Test the home page loads correctly"""
    response = test_client.get("/")
    assert response.status_code == 200
    assert b"Duck Collection Example" in response.data


def test_add_duck(test_client, test_db):
    """Test adding a duck to the database"""
    # Test data
    duck_data = {"name": "Test Duck", "type": "Rubber", "value": "10"}

    # Make POST request to add duck
    response = test_client.post(
        "/add_duck", json=duck_data, content_type="application/json"
    )

    # Check response
    assert response.status_code == 201
    assert b"Duck added successfully" in response.data

    # Verify duck was added to database
    saved_duck = test_db.find_one({"name": "Test Duck"})
    assert saved_duck is not None
    assert saved_duck["type"] == "Rubber"
    assert saved_duck["value"] == "10"


def test_find_duck(test_client, test_db):
    """Test finding a duck in the database"""
    # Add a test duck
    test_db.insert_one({"name": "Search Duck", "type": "Plastic", "value": "20"})

    # Search for the duck
    response = test_client.get("/find_duck?name=Search Duck")

    # Check response
    assert response.status_code == 200
    assert b"Search Duck" in response.data
    assert b"Plastic" in response.data
    assert b"20" in response.data


def test_find_nonexistent_duck(test_client):
    """Test searching for a duck that doesn't exist"""
    response = test_client.get("/find_duck?name=Nonexistent Duck")
    assert response.status_code == 404
    assert b"Duck not found" in response.data


def test_add_duck_missing_fields(test_client):
    """Test adding a duck with missing required fields"""
    # Test data with missing fields
    incomplete_data = {
        "name": "Incomplete Duck"
        # Missing type and value
    }

    response = test_client.post(
        "/add_duck", json=incomplete_data, content_type="application/json"
    )

    assert response.status_code == 400
