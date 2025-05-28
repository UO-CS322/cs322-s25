# Shakespearean Insult Generator with WTForms

This example demonstrates how to use Flask-WTF (WTForms) for form handling and validation in a Flask application. The application allows users to generate Shakespearean insults and manage the vocabulary used to create them.

## What you should be able to do with the new forms:
- Visit http://localhost:7005/vocabulary
- See the current vocabulary lists
- Add new words to any column
- See the updated lists after adding words

## Learning Objectives

1. Understand form handling in Flask using WTForms
2. Implement form validation
3. Create and use custom form classes
4. Handle form submission and display validation errors
5. Use flash messages for user feedback
6. Implement CSRF protection

## Project Structure

```
wtforms/
├── app.py              # Main Flask application
├── vocab.py           # Vocabulary data
├── templates/
│   ├── index.html     # Home page template
│   └── vocabulary.html # Vocabulary management template
└── README.md          # This file
```

## Key Concepts

### 1. Form Classes with WTForms

WTForms provides a way to define form classes that handle form creation, validation, and rendering. Here's an example from our application:

```python
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class VocabularyForm(FlaskForm):
    word = StringField('Word', validators=[
        DataRequired(),
        Length(min=2, max=50)
    ])
    column = StringField('Column (1, 2, or 3)', validators=[
        DataRequired(),
        Length(min=1, max=1)
    ])
    submit = SubmitField('Add Word')
```

### 2. Form Validation

WTForms provides built-in validators and allows for custom validation:

- `DataRequired()`: Ensures the field is not empty
- `Length()`: Validates the length of the input
- Custom validation can be added using the `validate_` prefix

### 3. CSRF Protection

Flask-WTF automatically handles CSRF protection. You need to:

1. Set a secret key in your Flask app:
```python
app.config['SECRET_KEY'] = 'your-secret-key-here'
```

2. Include the CSRF token in your forms:
```html
<form method="POST">
    {{ form.csrf_token }}
    <!-- form fields -->
</form>
```

### 4. Form Rendering in Templates

WTForms provides template helpers for rendering forms:

```html
<form method="POST">
    {{ form.csrf_token }}
    <div class="form-group">
        {{ form.word.label }}
        {{ form.word(class="form-control") }}
        {% if form.word.errors %}
            {% for error in form.word.errors %}
                <span style="color: red;">{{ error }}</span>
            {% endfor %}
        {% endif %}
    </div>
    {{ form.submit(class="btn") }}
</form>
```

### 5. Flash Messages

Use flash messages to provide feedback to users:

```python
from flask import flash

# In your route
flash('Successfully added word!', 'success')
```

```html
{% with messages = get_flashed_messages(with_categories=true) %}
    {% if messages %}
        {% for category, message in messages %}
            <div class="flash-message {{ category }}">
                {{ message }}
            </div>
        {% endfor %}
    {% endif %}
{% endwith %}
```

## Exercises (optional)

1. **Form Enhancement**
   - Add a dropdown field for column selection instead of a text input
   - Add a "Delete Word" feature with confirmation
   - Implement word editing functionality
   - Check for duplicate words in the same column (when adding)

2. **Validation**
   - Add custom validation to ensure words are unique
   - Add validation to prevent duplicate words across columns
   - Implement word format validation (e.g., only letters and hyphens)

3. **UI Improvements**
   - Add client-side validation using JavaScript
   - Implement a search feature for the vocabulary
   - Add pagination for long vocabulary lists

4. **Security**
   - Implement rate limiting for form submissions, e.g., no more than 10 words per minute
   - Implement logging for vocabulary changes
   - Use a database for user authentication and vocabulary storage

## Running the Application

1. Install dependencies:
```bash
pip install flask flask-wtf
```

2. Run the application:
```bash
python app.py
```

3. Visit `http://localhost:7005` in your browser

## Additional Resources

- [Flask-WTF Documentation](https://flask-wtf.readthedocs.io/)
- [WTForms Documentation](https://wtforms.readthedocs.io/)
- [Flask Documentation](https://flask.palletsprojects.com/)
