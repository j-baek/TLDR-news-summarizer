# Base image is Python 3.12
FROM python:3.12-slim

# Set the working directory in the container  to /app
WORKDIR /app

# Copy the requirement file into the container
COPY requirements.txt .

# Install dependencies from the requirements file 
# don't use the cache to always download the latest version
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the files from the current directory to the container
COPY . .

# expose port 3000 (local host) for Flask to run
EXPOSE 3000

# Command to run the application
CMD ["python3", "src/backend/main_flask.py"]