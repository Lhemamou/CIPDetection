# Use an official lightweight Python image.
FROM python:3.9-slim

# Set the working directory in the container.
WORKDIR /app

# Copy only the requirements.txt file to leverage Docker layer caching.
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application's source code from your host to your image filesystem.
COPY src/ .

# Set environment variables for Gradio credentials.
ENV GRADIO_USERNAME=default_username
ENV GRADIO_PASSWORD=default_password

# Make port 7860 available to the outside world.
EXPOSE 7860

# Run your Gradio application.
CMD ["python", "detection_cip.py"]