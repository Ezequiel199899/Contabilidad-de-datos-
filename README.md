 Spring Boot (8080)
   ↓ llama
Flask (5000).    vision-assist-ai/
│
├── backend-spring/
│   ├── Dockerfile
│   └── target/app.jar
│
├── backend-flask/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
└── docker-compose.yml.  b.   app.run(host="0.0.0.0", port=5000).    flask
numpy.      FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"].    FROM eclipse-temurin:17

WORKDIR /app

COPY target/app.jar app.jar

EXPOSE 8080

ENTRYPOINT ["java", "-jar", "app.jar"].       version: "3.9"

services:

  flask:
    build: ./backend-flask
    container_name: flask-service
    ports:
      - "5000:5000"

  spring:
    build: ./backend-spring
    container_name: spring-service
    ports:
      - "8080:8080"
    depends_on:
      - flask.       docker-compose up --build.    