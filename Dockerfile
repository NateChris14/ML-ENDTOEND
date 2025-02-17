# Creating a base image
FROM python:3.12

# Setting the working directory
WORKDIR /app

# Copying the application code
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV FLASK_APP=app.py
ENV PORT=8080

# Expose the required port
EXPOSE 8080

# Run the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
