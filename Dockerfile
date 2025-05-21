# Use the official Python image
FROM python:3.12

# Set the working directory inside the container
WORKDIR /ulogger_container

RUN pip install bumpversion

# Install pip tools
RUN pip install --upgrade pip build twine

# Copy the rest of your app code
COPY . .