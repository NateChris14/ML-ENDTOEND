#Creating a base image
FROM python:3.12

#Setting the working directory
WORKDIR /app

#Copying the application code
COPY . /app

#Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

#Exposing port
ENV PORT=5000
EXPOSE 5000

#Running the application:
CMD ["gunicorn","application:app"]