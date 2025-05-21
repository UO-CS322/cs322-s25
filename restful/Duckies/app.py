import os
from typing import Any, Dict, List, Optional, Union

from flask import Flask, Response, jsonify, render_template, request
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database


class DuckApp:
    def __init__(self, test_mode: bool = False) -> None:
        self.app = Flask(__name__)
        self.setup_database(test_mode)
        self.setup_routes()

    def setup_database(self, test_mode: bool) -> None:
        """Set up database connection"""
        if test_mode:
            # Use test database for testing
            self.client = MongoClient("localhost", 27017)
            self.db = self.client.test_duckdb
            self.collection = self.db.test_ducks
        else:
            # Use production database (in docker compose)
            mongodb_uri = os.environ.get("MONGODB_URI", "mongodb://localhost:27017")
            self.client = MongoClient(mongodb_uri)
            self.db = self.client.duckdb
            self.collection = self.db.ducks

    def setup_routes(self) -> None:
        """Set up Flask routes"""

        @self.app.route("/")
        def home() -> str:
            return render_template("index.html")

        # ----------------------------------------------------------------------
        # New RESTful endpoints
        # ----------------------------------------------------------------------
        @self.app.route("/ducks", methods=["GET"])
        def get_all_ducks() -> tuple[Response, int]:
            """Get all ducks in JSON format"""
            ducks = list(self.collection.find())
            for duck in ducks:
                duck["_id"] = str(duck["_id"])
            return jsonify(ducks), 200

        @self.app.route("/ducks/<name>", methods=["GET"])
        def get_duck(name: str) -> tuple[Response, int]:
            """Get a specific duck by name"""
            duck = self.collection.find_one({"name": name})
            if duck:
                duck["_id"] = str(duck["_id"])
                return jsonify(duck), 200
            return jsonify({"message": f"Duck '{name}' not found"}), 404

        @self.app.route("/ducks/<name>", methods=["PUT"])
        def update_duck(name: str) -> tuple[Response, int]:
            """Update a duck's information"""
            duck = self.collection.find_one({"name": name})
            if not duck:
                return jsonify({"message": f"Duck '{name}' not found"}), 404

            data = request.get_json()
            if not data:
                return jsonify({"error": "No data provided"}), 400

            # Update only provided fields
            update_data = {k: v for k, v in data.items() if k in ["type", "value"]}
            if not update_data:
                return jsonify({"error": "No valid fields to update"}), 400

            result = self.collection.update_one({"name": name}, {"$set": update_data})
            if result.modified_count > 0:
                return jsonify({"message": f"Duck '{name}' updated successfully"}), 200
            return jsonify({"message": "No changes made"}), 200

        @self.app.route("/ducks/<name>", methods=["DELETE"])
        def delete_duck(name: str) -> tuple[Response, int]:
            """Delete a duck"""
            result = self.collection.delete_one({"name": name})
            if result.deleted_count > 0:
                return jsonify({"message": f"Duck '{name}' deleted successfully"}), 200
            return jsonify({"message": f"Duck '{name}' not found"}), 404

        @self.app.route("/ducks/type/<duck_type>", methods=["GET"])
        def get_ducks_by_type(duck_type: str) -> tuple[Response, int]:
            """Get all ducks of a specific type"""
            ducks = list(self.collection.find({"type": duck_type}))
            for duck in ducks:
                duck["_id"] = str(duck["_id"])
            return jsonify(ducks), 200

        # ----------------------------------------------------------------------
        # Old end points -- not RESTful
        # ----------------------------------------------------------------------
        @self.app.route("/add_duck", methods=["POST"])
        def add_duck() -> tuple[Response, int]:
            # Get duck data from request
            duck = request.get_json()
            print(duck)

            # Validate required fields
            required_fields = ["name", "type", "value"]
            missing_fields = [
                field
                for field in required_fields
                if field not in duck or not duck[field]
            ]

            if missing_fields:
                return (
                    jsonify(
                        {
                            "error": f"Missing required fields: {', '.join(missing_fields)}"
                        }
                    ),
                    400,
                )

            # Remove test_marker from the duck data before storing
            duck.pop("test_marker", None)

            # Add duck to database
            self.collection.insert_one(duck)

            # Return success message
            return jsonify({"message": "Duck added successfully"}), 201

        @self.app.route("/find_duck", methods=["GET"])
        def find_duck() -> tuple[Response, int]:
            # Get search term from request
            name = request.args.get("name")

            # Search for duck in database
            duck = self.collection.find_one({"name": name})

            if duck:
                # Convert MongoDB document to JSON
                duck["_id"] = str(duck["_id"])
                return jsonify(duck), 200

            return jsonify({"message": "Duck not found"}), 404

        @self.app.route("/all_ducks", methods=["GET"])
        def all_ducks() -> str:
            # Get all ducks from database
            ducks = list(self.collection.find())
            # Convert ObjectId to string for each duck
            for duck in ducks:
                duck["_id"] = str(duck["_id"])
            return render_template("all_ducks.html", ducks=ducks)

    def run(self, host: str = "0.0.0.0", port: int = 6006, debug: bool = True) -> None:
        """Run the Flask application"""
        self.app.run(host=host, port=port, debug=debug)


# Create and run the application
if __name__ == "__main__":
    app = DuckApp()
    app.run()
