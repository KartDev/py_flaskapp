# Simple Flask App with MySQL

This is a simple Flask application that interacts with a MySQL database to store and retrieve information about persons.

## Prerequisites

- Docker

- Docker Compose

## Running the Application

1. Make sure Docker and Docker Compose are installed on your machine.

2. Open a terminal and navigate to the directory containing the `docker-compose.yml` file.

3. Run the following command to build the Docker images and start the containers:

	docker-compose up

The Flask application will be available at `http://localhost:5000`.


4. Use a tool like Postman or CURL to test the API endpoints:

- To create a person, send a POST request to `http://localhost:5000/persons` with a JSON payload containing the person's name and age:

  ```json

  {

    "name": "Arif",

    "age": 28

  }

  ```

- To fetch the list of persons, send a GET request to `http://localhost:5000/persons`.

5. To stop the containers and remove the resources (containers, networks, and volumes), run the following command:

	docker-compose down