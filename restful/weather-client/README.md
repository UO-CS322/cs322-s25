# Simple Python REST Client

Here's a simple example of a Python REST client that interacts with the `JSONPlaceholder`, which is a free fake REST API for testing and prototyping. This example demonstrates how to perform basic CRUD operations using the requests library.

First, make sure you have the requests library installed. You can install it using pip if you haven't done so:

```bash
pip install requests
```

```python
import requests

# Base URL for the JSONPlaceholder API
BASE_URL = 'https://jsonplaceholder.typicode.com/posts'

# Function to fetch all posts
def get_posts():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

# Function to create a new post
def create_post(title, body, userId):
    post_data = {
        'title': title,
        'body': body,
        'userId': userId
    }
    response = requests.post(BASE_URL, json=post_data)
    if response.status_code == 201:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

# Function to update a post
def update_post(post_id, title, body):
    post_data = {
        'title': title,
        'body': body,
        'userId': 1
    }
    response = requests.put(f"{BASE_URL}/{post_id}", json=post_data)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

# Function to delete a post
def delete_post(post_id):
    response = requests.delete(f"{BASE_URL}/{post_id}")
    if response.status_code == 200:
        print("Post deleted successfully.")
    else:
        print(f"Error: {response.status_code}")

# Example usage
if __name__ == "__main__":
    # Fetch all posts
    print("Fetching posts:")
    posts = get_posts()
    print(posts)

    # Create a new post
    print("\nCreating a new post:")
    new_post = create_post("My New Post", "This is the body of the new post.", 1)
    print(new_post)

    # Update a post (using id of the newly created post)
    if new_post:
        print("\nUpdating the newly created post:")
        updated_post = update_post(new_post['id'], "Updated Title", "Updated body content.")
        print(updated_post)

    # Delete the post
    if new_post:
        print("\nDeleting the new post:")
        delete_post(new_post['id'])
```

### Explanation:

**GET Request:** The `get_posts` function retrieves all posts from the server.
**POST Request:** The `create_post` function adds a new post to the server.
**PUT Request:** The `update_post` function updates an existing post by its ID.
**DELETE Request:** The `delete_pos`t function removes a post based on its ID.

You can run this script, and its main program will perform the operations defined in the functions, demonstrating how to interact with a REST API.

## A real-world example

Here’s an example script that retrieves the current weather for a specified city. 
The API documentation is a good example of how to document REST APIs: 
https://openweathermap.org/current

```python
import requests

# Your OpenWeatherMap API key (replace with your actual API key)
API_KEY = '69212516f61c4863e1fbacc7ce393c68'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    # Define the query parameters
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }

    # Send a GET request to the OpenWeatherMap API
    response = requests.get(BASE_URL, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON
        weather_data = response.json()
        return {
            'city': weather_data['name'],
            'temperature': weather_data['main']['temp'],
            'description': weather_data['weather'][0]['description'],
            'humidity': weather_data['main']['humidity'],
            'wind_speed': weather_data['wind']['speed']
        }
    else:
        print(f"Error: {response.status_code} - {response.reason}")
        return None

# Example usage
if __name__ == "__main__":
    city = input("Enter city name: ")
    weather_info = get_weather(city)

    if weather_info:
        print(f"Weather in {weather_info['city']}:")
        print(f"Temperature: {weather_info['temperature']}°C")
        print(f"Description: {weather_info['description']}")
        print(f"Humidity: {weather_info['humidity']}%")
        print(f"Wind Speed: {weather_info['wind_speed']} m/s")
```

### Explanation:
* API Key: Replace 'your_api_key' with your actual API key from OpenWeatherMap.
* GET Request: The get_weather function constructs a GET request to the OpenWeatherMap API, passing the city name and your API key as parameters.
  * Temperature Units: The units parameter specifies the measurement system; you can change from metric (Celsius) to imperial (Fahrenheit) if desired. Note - I couldn't get imperial units, but "standard" does return a different value.
* Error Handling: The program checks if the request was successful (HTTP status code 200). If not, it prints an error message.
* JSON Parsing: The response JSON is parsed to extract relevant weather information, which is then returned.

### Running the Example:

```
$ python weather.py
Enter city name: Eugene
Weather in Eugene:
Temperature: 32.25°C
Description: scattered clouds
Humidity: 91%
Wind Speed: 0.54 m/s
```

The complete response for Eugene was:
```json
{'coord': {'lon': -123.0867, 'lat': 44.0521}, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}], 'base': 'stations', 'main': {'temp': 32.25, 'feels_like': 32.25, 'temp_min': 32.25, 'temp_max': 33.73, 'pressure': 1025, 'humidity': 91, 'sea_level': 1025, 'grnd_level': 1002}, 'visibility': 10000, 'wind': {'speed': 0.54, 'deg': 258, 'gust': 0.74}, 'clouds': {'all': 30}, 'dt': 1732805437, 'sys': {'type': 2, 'id': 2001283, 'country': 'US', 'sunrise': 1732807482, 'sunset': 1732840607}, 'timezone': -28800, 'id': 5725846, 'name': 'Eugene', 'cod': 200}
```