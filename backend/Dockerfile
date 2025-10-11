FROM python:3.9-slim

# Set the working directory deep inside the container
WORKDIR /app

# Copy only the requirements file first to leverage Docker cache
COPY ./requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set the environment variable to find the Flask app
ENV FLASK_APP=server.py

# Expose the port
EXPOSE 5000

# Define the command to run the application
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]