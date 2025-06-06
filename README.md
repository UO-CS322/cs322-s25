# CS322-S25 Lecture Code

This repository contains code for in-lecture examples and exercises.

## Directory Structure

### [`flask/`](flask/)
Basic Flask application examples and tutorials. Contains simple Flask applications demonstrating core concepts like routing, templates, and forms.

### [`time_conversion/`](time_conversion/)
Time conversion utilities and examples. Contains:
- Time zone conversion
- Date formatting
- Time manipulation examples

### [`flask_js/`](flask_js/)
Advanced Flask application that combines Flask with JavaScript. Features:
- Shakespearean insult generator
- AJAX-based interactions
- Static file serving
- Template rendering

### [`mongo/`](mongo/)
MongoDB examples and exercises. Contains:
- Database connection examples
- CRUD operations
- Query examples
- MongoDB with Flask integration

### [`restful/`](restful/)
RESTful API examples and exercises:
- [`Duckies/`](restful/Duckies/): A RESTful API for managing a collection of rubber ducks
  - Everything in the `mongo/Duckies/` + new RESTful endpoints
- [`Shakespeare/`](restful/Shakespeare/): Shakespearean insult generator as a RESTful API
  - [An in-class exercise to convert a small Flask application into a RESTful API](restful/Shakespeare/RESTfulExercise.md)

### [`wtforms/`](wtforms/)
Form handling and validation examples using Flask-WTF. Features:
- Shakespearean insult generator with vocabulary management
- Form validation and error handling
- CSRF protection
- Flash messages
- Static file organization
- [Intro to form handling in Flask using WTForms](wtforms/README.md)

### Documentation
- [RESTNaming.md](RESTNaming.md): A guide to RESTful naming conventions

### Week 10: Final Review

The final review materials include:

1. **Mock Interview Materials**
   - Yellow team interview questions and guidelines
   - Interview preparation resources

2. **DRY Refactoring Exercises**
   Located in `w10/final-review/`, these exercises demonstrate the "Don't Repeat Yourself" principle through three practical examples:
   - Command Handler: Refactoring if-elif-else statements
   - Number Processor: Refactoring repeated loop patterns
   - Restaurant Rating System: Refactoring complex data processing

   Each exercise includes:
   - Original implementation with repetitive code
   - Refactored version demonstrating DRY principles
   - Clear examples of how to improve code maintainability

   See `w10/final-review/README.md` for detailed instructions and learning objectives.

