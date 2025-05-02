
## Midterm review examples

Here’s a simple AJAX example demonstrating how to handle typed character events using Flask and jQuery. In this example, we’ll create a Flask server that responds to user input from a text field, sending back a response with the typed character count.

### Step 1: Set Up Flask

First, ensure you have Flask installed. You can install it using pip if you haven't done it yet:

**bash**

```
pip install Flask
```

Here's a simple Flask application (`app.py`):

**python**

```
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/count', methods=['POST'])
def count_characters():
    data = request.json
    text = data.get('text', '')
    character_count = len(text)
    return jsonify({'count': character_count})

if __name__ == '__main__':
    app.run(debug=True)
```

### Step 2: Create HTML with jQuery

Next, create an HTML file (e.g., `index.html`) that will handle the user input:

**html**

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Character Count with AJAX</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>

<h2>Type something:</h2>
<input type="text" id="textInput">
<p id="output"></p>

<script>
$(document).ready(function() {
    $('#textInput').on('input', function() {
        var inputText = $(this).val();
      
        $.ajax({
            type: 'POST',
            url: '/count',
            contentType: 'application/json',
            data: JSON.stringify({ text: inputText }),
            success: function(response) {
                $('#output').text('Character count: ' + response.count);
            },
            error: function() {
                $('#output').text('Error processing your request.');
            }
        });
    });
});
</script>

</body>
</html>
```

### Step 3: Run the Application

1. Start the Flask server by running `app.py`:

**bash**

```
python app.py
```

2. Open your web browser and go to `http://127.0.0.1:5000`.
3. Open the `index.html` file in your browser.

### How It Works

* The user types into the text field. For every input event, jQuery sends an AJAX POST request to the `/count` endpoint.
* The server counts the characters in the input text and responds with that count.
* The client displays the character count dynamically below the input field.

This example effectively demonstrates handling typed character events with an AJAX call in a Flask application. You can expand upon this basic structure with more complex logic or additional features as needed.

modify the example to avoid using POST

GPT-4o

Certainly! If you'd like to modify the example to avoid using the POST method, you can use the GET method instead. In this case, we'll send the text input as a query parameter in the URL. Here’s the updated example:

### Step 1: Update Flask Application

Here's the modified Flask application (`app.py`) that handles GET requests:

**python**

```
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/count', methods=['GET'])
def count_characters():
    text = request.args.get('text', '')
    character_count = len(text)
    return jsonify({'count': character_count})

if __name__ == '__main__':
    app.run(debug=True)
```

### Step 2: Update HTML with jQuery

Next, update the HTML file (e.g., `index.html`) to use a GET request:

**html**

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Character Count with AJAX GET</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>

<h2>Type something:</h2>
<input type="text" id="textInput">
<p id="output"></p>

<script>
$(document).ready(function() {
    $('#textInput').on('input', function() {
        var inputText = $(this).val();
      
        $.ajax({
            type: 'GET',
            url: '/count',
            data: { text: inputText },
            success: function(response) {
                $('#output').text('Character count: ' + response.count);
            },
            error: function() {
                $('#output').text('Error processing your request.');
            }
        });
    });
});
</script>

</body>
</html>
```

### How It Works

* In this modified example, the user still types into the text field. For every input event, jQuery sends an AJAX GET request to the `/count` endpoint.
* The input text is now sent as a query parameter instead of in the body of a POST request.
* The server counts the characters in the input text and responds with that count as before.
* The client displays the character count dynamically below the input field.

### Step 3: Run the Application

1. Start the updated Flask server by running `app.py`:

**bash**

```
python app.py
```

2. Open your web browser and go to `http://127.0.0.1:5000`.
3. Open or refresh the `index.html` file in your browser.

Using GET for this example allows you to retrieve the character count in a more straightforward manner, while maintaining the functionality of the application.
