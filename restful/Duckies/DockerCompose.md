# Docker Compose Super Quick Start

Docker Compose lets you run multiple containers together. For our Duckies app, we need two containers:
1. A Flask web app
2. A MongoDB database

## Run the App

```bash
# Start the app and database
docker-compose up

# Stop everything when you're done
docker-compose down

# View logs
docker-compose logs

# Rebuild containers
docker-compose up --build
```

## What's Happening

Our `docker-compose.yml` runs two things:

```yaml
services:
  mongodb:
    image: mongo:latest
    ports:
      - "27017:27017"
    volumes:
      - mongodb_data:/data/db

  app:
    build: .
    ports:
      - "5005:5005"
    environment:
      - MONGODB_URI=mongodb://mongodb:27017/
    depends_on:
      - mongodb
```

- The Flask app runs on http://localhost:5005
- MongoDB runs on port 27017
- Your data stays in the `mongodb_data` volume

## Useful Commands

```bash
# Start in background
docker-compose up -d

# See what's happening
docker-compose logs

# Rebuild after changes
docker-compose up --build
```

## If Something's Wrong

1. Port 5005 already in use? Change it in `docker-compose.yml`
2. Can't connect to MongoDB? Check if both containers are running:
   ```bash
   docker-compose ps
   ```
3. Lost your data? It's in the `mongodb_data` volume

## More Info

- [Docker Compose docs](https://docs.docker.com/compose/)
