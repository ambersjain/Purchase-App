# Use the official Python base image from Docker Hub
FROM python:3.9.6-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app


# Install any dependencies specified in requirements.txt
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy data
COPY purchases_v1.json /app/purchases_v1.json

# Set the command to run your Python script
CMD ["python3", "process_purchase.py"]
