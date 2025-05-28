# This Dockerfile creates a container for a Flask application that insults you
# Build with `docker build -t affront .`
# Run with `docker run -p 7005:7005 affront`

FROM python:3.12-slim
LABEL maintainer="Boyana Norris <norris@cs.uoregon.edu>"

# Copy all files in the current directory to /insulter in the container
COPY . /insulter
WORKDIR /insulter

# Install dependencies
RUN pip install flask

# Export port 7007
EXPOSE 7007

# Run the application
ENTRYPOINT ["python", "app.py"]
