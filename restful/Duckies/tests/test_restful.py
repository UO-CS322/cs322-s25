from typing import Dict, Any, List, cast
import pytest
from flask.testing import FlaskClient
from app import DuckApp


@pytest.fixture
def client() -> FlaskClient:
    """Create a test client for the app"""
    app = DuckApp(test_mode=True)
    # Clear the test database before each test
    app.collection.delete_many({})
    return app.app.test_client()


@pytest.fixture
def sample_duck() -> Dict[str, Any]:
    """Sample duck data for testing"""
    return {
        "name": "test_duck",
        "type": "collectible",
        "value": 10,
        "test_marker": True,
    }


def test_get_all_ducks_empty(client: FlaskClient) -> None:  # noqa
    """Test getting all ducks when database is empty"""
    response = client.get("/ducks")
    assert response.status_code == 200
    data = cast(List[Dict[str, Any]], response.json)
    assert data == []


def test_get_all_ducks_with_data(
    client: FlaskClient, sample_duck: Dict[str, Any]  # noqa
) -> None:
    """Test getting all ducks when database has data"""
    # Add a test duck
    client.post("/add_duck", json=sample_duck)

    # Get all ducks
    response = client.get("/ducks")
    assert response.status_code == 200
    data = cast(List[Dict[str, Any]], response.json)
    assert len(data) == 1
    assert data[0]["name"] == sample_duck["name"]
    assert data[0]["type"] == sample_duck["type"]
    assert data[0]["value"] == sample_duck["value"]


def test_get_duck_not_found(client: FlaskClient) -> None:  # noqa
    """Test getting a non-existent duck"""
    response = client.get("/ducks/nonexistent")
    assert response.status_code == 404
    data = cast(Dict[str, Any], response.json)
    assert data["message"] == "Duck 'nonexistent' not found"


def test_get_duck_found(
    client: FlaskClient, sample_duck: Dict[str, Any]
) -> None:  # noqa
    """Test getting an existing duck"""
    # Add a test duck
    client.post("/add_duck", json=sample_duck)

    # Get the duck
    response = client.get(f"/ducks/{sample_duck['name']}")
    assert response.status_code == 200
    data = cast(Dict[str, Any], response.json)
    assert data["name"] == sample_duck["name"]
    assert data["type"] == sample_duck["type"]
    assert data["value"] == sample_duck["value"]


def test_update_duck_not_found(client: FlaskClient) -> None:  # noqa
    """Test updating a non-existent duck"""
    response = client.put("/ducks/nonexistent", json={"type": "new_type"})
    assert response.status_code == 404
    data = cast(Dict[str, Any], response.json)
    assert data["message"] == "Duck 'nonexistent' not found"


def test_update_duck_no_data(
    client: FlaskClient, sample_duck: Dict[str, Any]
) -> None:  # noqa
    """Test updating a duck with no data"""
    # Add a test duck
    client.post("/add_duck", json=sample_duck)

    # Try to update with no data
    response = client.put(f"/ducks/{sample_duck['name']}", json={})
    assert response.status_code == 400
    data = cast(Dict[str, Any], response.json)
    assert data["error"] == "No data provided"


def test_update_duck_invalid_fields(
    client: FlaskClient, sample_duck: Dict[str, Any]  # noqa
) -> None:
    """Test updating a duck with invalid fields"""
    # Add a test duck
    client.post("/add_duck", json=sample_duck)

    # Try to update with invalid field
    response = client.put(
        f"/ducks/{sample_duck['name']}", json={"invalid_field": "value"}
    )
    assert response.status_code == 400
    data = cast(Dict[str, Any], response.json)
    assert data["error"] == "No valid fields to update"


def test_update_duck_success(
    client: FlaskClient, sample_duck: Dict[str, Any]
) -> None:  # noqa
    """Test successfully updating a duck"""
    # Add a test duck
    client.post("/add_duck", json=sample_duck)

    # Update the duck
    update_data = {"type": "new_type", "value": 20}
    response = client.put(f"/ducks/{sample_duck['name']}", json=update_data)
    assert response.status_code == 200
    data = cast(Dict[str, Any], response.json)
    assert data["message"] == f"Duck '{sample_duck['name']}' updated successfully"

    # Verify the update
    get_response = client.get(f"/ducks/{sample_duck['name']}")
    assert get_response.status_code == 200
    data = cast(Dict[str, Any], get_response.json)
    assert data["type"] == update_data["type"]
    assert data["value"] == update_data["value"]


def test_delete_duck_not_found(client: FlaskClient) -> None:  # noqa
    """Test deleting a non-existent duck"""
    response = client.delete("/ducks/nonexistent")
    assert response.status_code == 404
    data = cast(Dict[str, Any], response.json)
    assert data["message"] == "Duck 'nonexistent' not found"


def test_delete_duck_success(
    client: FlaskClient, sample_duck: Dict[str, Any]
) -> None:  # noqa
    """Test successfully deleting a duck"""
    # Add a test duck
    client.post("/add_duck", json=sample_duck)

    # Delete the duck
    response = client.delete(f"/ducks/{sample_duck['name']}")
    assert response.status_code == 200
    data = cast(Dict[str, Any], response.json)
    assert data["message"] == f"Duck '{sample_duck['name']}' deleted successfully"

    # Verify the duck is gone
    get_response = client.get(f"/ducks/{sample_duck['name']}")
    assert get_response.status_code == 404


def test_get_ducks_by_type_empty(client: FlaskClient) -> None:  # noqa
    """Test getting ducks by type when none exist"""
    response = client.get("/ducks/type/collectible")
    assert response.status_code == 200
    data = cast(List[Dict[str, Any]], response.json)
    assert data == []


def test_get_ducks_by_type_with_data(
    client: FlaskClient, sample_duck: Dict[str, Any]  # noqa
) -> None:
    """Test getting ducks by type when some exist"""
    # Add a test duck
    client.post("/add_duck", json=sample_duck)

    # Get ducks by type
    response = client.get(f"/ducks/type/{sample_duck['type']}")
    assert response.status_code == 200
    data = cast(List[Dict[str, Any]], response.json)
    assert len(data) == 1
    assert data[0]["name"] == sample_duck["name"]
    assert data[0]["type"] == sample_duck["type"]
