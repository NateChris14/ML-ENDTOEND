# Use Python 3.12 base image
FROM python:3.12

# Set the working directory
WORKDIR /app

# Copy application files
COPY . /app

# Upgrade pip and install dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV PORT=8080

# Expose the required port
EXPOSE 8080

# Run the Flask app
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=8080"]
