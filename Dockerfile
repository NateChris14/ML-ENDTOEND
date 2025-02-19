# Use Python 3.12 base image
FROM python:3.12-slim

# Set a non-root user
RUN groupadd -r appgroup && useradd -r -g appgroup appuser

# Set the working directory
WORKDIR /app

# Copy application files
COPY . /app

# Upgrade pip and install dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV FLASK_RUN_HOST=0.0.0.0
ENV PORT=8080

# Expose the required port
EXPOSE 8080

# Change ownership and switch to non-root user
RUN chown -R appuser:appgroup /app
USER appuser

# Run the Flask app
CMD ["flask", "run", "--port=8080"]

