# @file: app.py
# @brief: This is a simple Flask application that generates random Shakespearean insults.

import random
from flask import Flask, render_template

import vocab

# Instantiate the Flask application
app = Flask(__name__)

def generate_insult():
    """Generate a random Shakespearean insult.
    This function randomly selects words from three columns of a vocabulary
    list and combines them into a Shakespearean-style insult.
    The insult is prefixed with "Thou" and ends with an exclamation mark.

    Returns:
        str: A randomly generated Shakespearean insult.
    """
    insult = "Thou "
    insult += random.choice(vocab.column1) + " "
    insult += random.choice(vocab.column2) + " "
    insult += random.choice(vocab.column3) + "!"
    return insult
    
@app.route('/')
def index():
    return "Have a nice day!"

@app.route('/insultme')
def insulter():
    """Generate and display a Shakespearean insult in the index.html template.
    This function gets invoked if you browse to the /insultme URL, e.g., http://127.0.1:5005/insultme
    
    @return: Rendered HTML template index.html (in the templates/ directory)
    """
    some_insult = generate_insult()
    return render_template("index.html", insult=some_insult)

if __name__ == '__main__':
    # Run the Flask application on the local server on port 5005
    # with debug mode enabled.
    app.run(debug=True, host='0.0.0.0', port=7005)