#Creating a base image
FROM python:3.12

#Setting the working directory
WORKDIR /app

#Copying the application code
COPY . /app

RUN apt update -y && apt install awscli -y
#Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

#Running the application:
CMD ["python3","app:app"]