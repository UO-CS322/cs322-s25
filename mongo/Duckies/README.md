# Rubber Duckies Example

This is a simple Flask application with a MongoDB backend that demonstrates basic database operations and web development concepts.

* MongoDB notes: [Mongodb.md](./Mongodb.md)
* Docker compose notes: [DockerCompose.md](./DockerCompose.md)

## Project Structure
```
├── DockerCompose.md : composes the `web` and `db` services in this example
├── Dockerfile : Container for the Flask application
├── app.ini : Configuration used in multiple components (e.g., port)
├── app.py : Flask application for adding and finding ducks in the database
├── requirements.txt : required python packages (install in a `venv`)
├── selenium_test.py : test cases for the application's functionality
└── templates
    └── index.html : the web interface with AJAX scripts
```

## Features
- Add duckies to the MongoDB database
- Search for duckies by name
- Simple and intuitive web interface
- AJAX-based interactions
- Docker support for easy deployment

## Testing
The application includes Selenium tests that demonstrate how to:
- Test web interfaces programmatically
- Simulate user interactions
- Verify database operations
- Handle AJAX responses

See `selenium_test.py` for example test cases.

## Getting Started
1. Install dependencies: `pip install -r requirements.txt`
2. Start MongoDB
3. Run the application: `python app.py`
4. Access the web interface at `http://localhost:5005`

To run the pytests:
```bash
(venv) ➜  Duckies git:(main) ✗ pytest tests
Test session starts (platform: darwin, Python 3.10.15, pytest 7.4.3, pytest-sugar 0.9.7)
rootdir: /Users/norris/teaching/cs322-s25/mongo/Duckies
plugins: hypothesis-6.99.11, anyio-4.3.0, cov-4.1.0, xprocess-1.0.2, sugar-0.9.7
collected 7 items                                                                    

 tests/test_flask.py ✓✓✓✓✓                                              71% ███████▎  
 tests/test_selenium.py ✓✓                                             100% ██████████

Results (10.73s):
       7 passed
``` 

## Docker Support
The application can be run using Docker Compose:
```bash
docker-compose up
```

This will start both the Flask application and MongoDB in separate containers.

## Starting MongoDB

Below are simple instructions for installing MongoDB on macOS and Ubuntu/Debian. For more complete and up to date instructions, see the [official MongoDB documentation](https://www.mongodb.com/docs/manual/installation/).

### macOS
1. Install MongoDB using Homebrew:
   ```bash
   brew tap mongodb/brew
   brew install mongodb-community
   ```
2. Start MongoDB service:
   ```bash
   brew services start mongodb-community
   ```
3. Stop MongoDB service (when needed):
   ```bash
   brew services stop mongodb-community
   ```
4. Check if MongoDB is running:
   ```bash
   brew services list | grep mongodb
   # Should show "started" status
   
   # Or connect to MongoDB shell to verify:
   mongosh
   # If connection is successful, MongoDB is running
   ```

### Linux (Ubuntu/Debian)
1. Import MongoDB public GPG key:
   ```bash
   curl -fsSL https://pgp.mongodb.com/server-7.0.asc | \
   sudo gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg \
   --dearmor
   ```
2. Create list file for MongoDB:
   ```bash
   echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list
   ```
3. Update package database:
   ```bash
   sudo apt-get update
   ```
4. Install MongoDB:
   ```bash
   sudo apt-get install -y mongodb-org
   ```
5. Start MongoDB:
   ```bash
   sudo systemctl start mongod
   ```
6. Enable MongoDB to start on boot:
   ```bash
   sudo systemctl enable mongod
   ```
7. Check if MongoDB is running:
   ```bash
   # Check service status
   sudo systemctl status mongod
   # Should show "active (running)"
   
   # Or connect to MongoDB shell to verify:
   mongosh
   # If connection is successful, MongoDB is running
   ```

### Windows
1. Download MongoDB Community Server from the [official website](https://www.mongodb.com/try/download/community)
2. Run the installer and follow the installation wizard
3. MongoDB will be installed as a Windows service and will start automatically
4. Check if MongoDB is running:
   ```bash
   # Open Command Prompt as Administrator and check service status:
   sc query MongoDB
   # Should show "RUNNING" state
   
   # Or connect to MongoDB shell to verify:
   "C:\Program Files\MongoDB\Server\7.0\bin\mongosh.exe"
   # If connection is successful, MongoDB is running
   ```

### Verifying MongoDB Connection
Regardless of your operating system, you can verify MongoDB is running by:
1. Opening a terminal/command prompt
2. Running the MongoDB shell:
   ```bash
   mongosh
   ```
3. If you see a prompt like this, MongoDB is running:
   ```
   Current Mongosh Log ID: ...
   Connecting to:          mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.1.1
   Using MongoDB:          7.0.x
   Using Mongosh:          2.1.1
   ...
   >
   ```
4. Try a simple command to verify the connection:
   ```bash
   > show dbs
   ```

### Docker Compose Help

### Official Documentation
For detailed installation and configuration instructions, refer to the official MongoDB documentation:
- [Install MongoDB Community Edition](https://www.mongodb.com/docs/manual/installation/)
- [Install MongoDB on macOS](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-os-x/)
- [Install MongoDB on Ubuntu](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/)
- [Install MongoDB on Windows](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-windows/)

# Duckies Application

A Flask application for managing a collection of rubber ducks, with MongoDB as the database.

## Prerequisites

- Docker Desktop for Mac
- Homebrew (for installing Docker)

## Installation

1. Install Docker Desktop using Homebrew:
   ```bash
   brew install --cask docker
   ```

2. Start Docker Desktop:
   - Open Docker Desktop from your Applications folder
   - Wait for Docker to start (you'll see the whale icon in your menu bar)

## Running the Application

1. Build and start the containers:
   ```bash
   docker-compose up --build
   ```

2. The application will be available at:
   - Web interface: http://localhost:5005
   - MongoDB: mongodb://localhost:27017

## Development

- The application code is in `app.py`
- MongoDB data is persisted in a Docker volume

## Additional Resources

- [Docker Desktop for Mac Documentation](https://docs.docker.com/desktop/mac/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [MongoDB Docker Image](https://hub.docker.com/_/mongo)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Selenium Documentation](https://selenium-python.readthedocs.io/)

## Troubleshooting

1. If you get a port conflict:
   - Check if another service is using port 5005
   - Modify the port in `docker-compose.yml` if needed

2. If MongoDB connection fails:
   - Ensure Docker Desktop is running
   - Check if the MongoDB container is running: `docker-compose ps`
   - View logs: `docker-compose logs mongodb`

3. For Selenium test issues:
   - Check Chrome and ChromeDriver versions match
   - View test logs: `docker-compose logs app`
