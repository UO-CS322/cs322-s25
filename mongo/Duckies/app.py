from flask import Flask, jsonify, render_template, request
from pymongo import MongoClient
import os


class DuckApp:
    def __init__(self, test_mode=False):
        self.app = Flask(__name__)
        self.setup_database(test_mode)
        self.setup_routes()

    def setup_database(self, test_mode):
        """Set up database connection"""
        if test_mode:
            # Use test database for testing
            self.client = MongoClient("localhost", 27017)
            self.db = self.client["test_duckdb"]
            self.collection = self.db["test_ducks"]
        else:
            # Use production database (in docker compose)
            mongodb_uri = os.environ.get("MONGODB_URI", "mongodb://localhost:27017")
            self.client = MongoClient(mongodb_uri)
            self.db = self.client["duckdb"]
            self.collection = self.db["ducks"]

    def setup_routes(self):
        """Set up Flask routes"""

        @self.app.route("/")
        def home():
            return render_template("index.html")

        @self.app.route("/add_duck", methods=["POST"])
        def add_duck():
            # Get duck data from request
            duck = request.get_json()

            # Remove test_marker from the duck data before storing
            duck.pop("test_marker", None)

            # Add duck to database
            self.collection.insert_one(duck)

            # Return success message
            return jsonify({"message": "Duck added successfully"}), 201

        @self.app.route("/find_duck", methods=["GET"])
        def find_duck():
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
        def all_ducks():
            ducks = list(self.collection.find())
            # Convert ObjectId to string for each duck
            for duck in ducks:
                duck["_id"] = str(duck["_id"])
            return jsonify({"success": True, "ducks": ducks})

    def run(self, host="0.0.0.0", port=6006, debug=True):
        """Run the Flask application"""
        self.app.run(host=host, port=port, debug=debug)


# Create and run the application
if __name__ == "__main__":
    app = DuckApp()
    app.run()
