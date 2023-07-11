# Use an official Python runtime as the base image
FROM python:3.9

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgomp1 \
    build-essential \
    && rm -rf /var/lib/apt/lists/*


# Set the working directory inside the container
WORKDIR /app

# Copy the Python script and requirements.txt file to the container
COPY watch_next.py requirements.txt ./

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Download the spaCy English model
RUN python -m spacy download en_core_web_lg

# Set the command to run your script
CMD ["python", "watch_next.py"]
