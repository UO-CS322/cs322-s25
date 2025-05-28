"""User management module for the Shakespearean insult generator.

This module provides user authentication and management functionality using Flask-Login.
It implements a simple file-based user storage system with secure password hashing.

Note on Mixin classes:
A mixin class is a design pattern in object-oriented programming that provides a way
to reuse code across multiple classes. What is it? A mixin is a class that contains
methods and properties that can be "mixed in" to other classes. It's not meant to be
instantiated on its own but provides functionality that can be reused across different
classes that are not necessarily part of the same hierarchy.
"""

import json
import os
from typing import Dict, Optional

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# File path for user data persistence
USER_DATA_FILE = "user_data.json"

# Simple in-memory user storage with file persistence
users: Dict[str, "User"] = {}


def load_users():
    """Load users from the JSON file if it exists."""
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            for username, user_data in data.items():
                user = User(username, user_data["password_hash"], is_hash=True)
                users[username] = user


def save_users():
    """Save users to the JSON file."""
    data = {
        username: {"password_hash": user.password_hash}
        for username, user in users.items()
    }
    with open(USER_DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f)


class User(UserMixin):
    """User class for authentication and user management.

    This class implements user authentication functionality by inheriting from Flask-Login's UserMixin.
    UserMixin provides default implementations for the methods that Flask-Login expects user objects to have:
    - is_authenticated: property that is True if the user has valid credentials
    - is_active: property that is True if the user's account is active
    - is_anonymous: property that is False for regular users
    - get_id(): method that returns a unique identifier for the user

    The class also implements secure password hashing using Werkzeug's security functions.

    Attributes:
        id (str): The user's unique identifier (username)
        username (str): The user's username
        password_hash (str): The hashed version of the user's password
    """

    def __init__(self, username: str, password: str, is_hash: bool = False) -> None:
        """Initialize a new user with a username and password.

        Args:
            username: The user's username
            password: The user's plain text password (will be hashed) or existing hash
            is_hash: Whether the password parameter is already a hash
        """
        self.id = username
        self.username = username
        self.password_hash = password if is_hash else generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        """Verify if the provided password matches the stored hash.

        Args:
            password: The plain text password to verify

        Returns:
            True if the password matches, False otherwise
        """
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def get(user_id: str) -> Optional["User"]:
        """Retrieve a user by their ID.

        Args:
            user_id: The user's ID (username)

        Returns:
            The user object if found, None otherwise
        """
        return users.get(user_id)

    @staticmethod
    def create(username: str, password: str) -> Optional["User"]:
        """Create a new user if the username is not already taken.

        Args:
            username: The desired username
            password: The user's plain text password

        Returns:
            The newly created user object if successful, None if username exists
        """
        if username in users:
            return None
        user = User(username, password)
        users[username] = user
        save_users()  # Save users after creating a new one
        return user


# Load existing users after the User class is defined
load_users()
