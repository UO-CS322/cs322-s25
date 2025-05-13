# Docker Compose Super Quick Start

Docker Compose lets you run multiple containers together. For our Duckies app, we need two containers:
1. A Flask web app
2. A MongoDB database

## Basic Commands

```bash
# Start everything
docker-compose up

# Start in background
docker-compose up -d

# Stop everything
docker-compose down

# View logs
docker-compose logs

# Rebuild containers
docker-compose up --build
```

## How It Works

Our `docker-compose.yml` defines two services:

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

- `mongodb`: Uses the official MongoDB image
- `app`: Builds from our Dockerfile
- `ports`: Maps container ports to your machine
- `volumes`: Persists MongoDB data
- `environment`: Sets connection string for MongoDB

## Key Concepts

1. **Services**: Each container is a service (mongodb, app)
2. **Networking**: Services can talk using service names
3. **Volumes**: Persistent data storage
4. **Environment**: Configuration via environment variables

## Common Issues

1. **Port conflicts**: Change port numbers in `docker-compose.yml`
2. **Connection issues**: Check service names match
3. **Data persistence**: Data in volumes survives container restarts

## Learn More

- [Docker Compose Documentation](https://docs.docker.com/compose/)
