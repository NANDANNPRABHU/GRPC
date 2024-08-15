# Use Debian as a base image
FROM debian:bullseye-slim

# Set the working directory in the container
WORKDIR /workspace

# Install Python, Git, and any other dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies from requirements.txt
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
