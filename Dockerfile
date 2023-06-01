# Use a base image with Python pre-installed
FROM python:3.9
# Set the working directory inside the container
WORKDIR /fastapi-app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the project dependencies
RUN pip install -r requirements.txt

# Copy the entire project directory to the container
COPY ./app ./app


# Define the command to start the FastAPI application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8051"]

