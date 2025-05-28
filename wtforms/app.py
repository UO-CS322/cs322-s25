"""Shakespearean Insult Generator Flask Application.

This module implements a Flask web application that generates random Shakespearean insults
and provides user authentication and vocabulary management functionality.
"""

import configparser
import random
from pathlib import Path

from flask import Flask, flash, redirect, render_template, url_for
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

import vocab
from forms import LoginForm, RegisterForm
from models import User

# Load configuration
config = configparser.ConfigParser()
config.read(Path(__file__).parent / "app.ini")

# Initialize Flask application
app = Flask(__name__)
app.config["SECRET_KEY"] = config["app"]["SECRET_KEY"]

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = config["login"]["LOGIN_VIEW"]
login_manager.login_message = config["login"]["LOGIN_MESSAGE"]
login_manager.login_message_category = config["login"]["LOGIN_MESSAGE_CATEGORY"]


@login_manager.user_loader
def load_user(user_id):
    """Load a user from the user ID stored in the session."""
    return User.get(user_id)


class VocabularyForm(FlaskForm):
    """Form for adding new vocabulary words."""

    word = StringField(
        "Word",
        validators=[
            DataRequired(),
            Length(min=2, max=50, message="Word must be between 2 and 50 characters"),
        ],
    )
    column = StringField(
        "Column (1, 2, or 3)",
        validators=[
            DataRequired(),
            Length(min=1, max=1, message="Column must be 1, 2, or 3"),
        ],
    )
    submit = SubmitField("Add Word")


def generate_insult():
    """Generate a random Shakespearean insult."""
    return f"Thou {random.choice(vocab.column1)} {random.choice(vocab.column2)} {random.choice(vocab.column3)}!"


@app.route("/")
def index():
    """Render the home page."""
    return render_template("index.html")


@app.route("/insultme")
def insulter():
    """Generate and display a Shakespearean insult."""
    return render_template("index.html", insult=generate_insult())


@app.route("/login", methods=["GET", "POST"])
def login():
    """Handle user login."""
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.get(form.username.data)
        if user and user.check_password(form.password.data):
            login_user(user)
            flash("Logged in successfully!", "success")
            return redirect(url_for("vocabulary"))
        flash("Invalid username or password", "error")
    return render_template("login.html", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Handle user registration."""
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    form = RegisterForm()
    if form.validate_on_submit():
        user = User.create(form.username.data, form.password.data)
        if user:
            login_user(user)
            flash("Registration successful!", "success")
            return redirect(url_for("vocabulary"))
        flash("Username already exists", "error")
    return render_template("register.html", form=form)


@app.route("/logout")
@login_required
def logout():
    """Handle user logout."""
    logout_user()
    flash("Logged out successfully!", "success")
    return redirect(url_for("index"))


@app.route("/vocabulary", methods=["GET", "POST"])
@login_required
def vocabulary():
    """Handle vocabulary management."""
    form = VocabularyForm()
    if form.validate_on_submit():
        word = form.word.data
        column = form.column.data

        if column not in ["1", "2", "3"]:
            flash("Column must be 1, 2, or 3", "error")
            return redirect(url_for("vocabulary"))

        vocab_list = [vocab.column1, vocab.column2, vocab.column3][int(column) - 1]
        vocab_list.append(word)
        flash(f'Successfully added "{word}" to column {column}!', "success")
        return redirect(url_for("vocabulary"))

    return render_template("vocabulary.html", form=form, vocab=vocab)


if __name__ == "__main__":
    app.run(
        debug=config["app"].getboolean("DEBUG"),
        host=config["app"]["HOST"],
        port=config["app"].getint("PORT"),
    )
