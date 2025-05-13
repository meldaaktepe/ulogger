# Use the official Python image
FROM python:3.12

# Set the working directory inside the container
WORKDIR /ulogger

# Copy requirements.txt and install Python libraries
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your app code
COPY . .