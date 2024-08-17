# Use an official Python runtime as a parent image
FROM python:3.12

LABEL maintainer="wania-kazmi"
# Set the working directory in the container
WORKDIR /code
# Install system dependencies required for potential Python packages
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install poetry

# Copy the current directory contents into the container at /code
COPY . /code/

# Configuration to avoid creating virtual environments inside the Docker container
RUN poetry config virtualenvs.create false

# Install dependencies including development ones
RUN poetry install

# Make port 8000 available to the world outside this container
EXPOSE 8001

# Run the app. CMD can be overridden when starting the container
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0","--port", "8001","--reload"]















# # Use an official Python runtime as a parent image
# FROM python:3.12

# LABEL maintainer="wania-kazmi"

# # Set the working directory in the container
# WORKDIR /code

# # Install system dependencies required for potential Python packages
# RUN apt-get update && apt-get install -y \
#     build-essential \
#     libpq-dev \
#     protobuf-compiler \
#     wget \
#     ca-certificates \
#     && rm -rf /var/lib/apt/lists/*

# # Install Poetry
# RUN pip install poetry

# # Copy only the pyproject.toml and poetry.lock files to the container
# COPY pyproject.toml poetry.lock /code/

# # Configuration to avoid creating virtual environments inside the Docker container
# RUN poetry config virtualenvs.create false

# # Install dependencies including development ones
# RUN poetry install

# # Copy the rest of the application code to the container
# COPY . /code/

# # Make port 8001 available to the world outside this container
# EXPOSE 8001

# # Run the app
# CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001", "--reload"]