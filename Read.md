

# FastAPI CRUD API for Book Management

This is a CRUD (Create, Read, Update, Delete) API developed using the FastAPI framework in Python for managing a collection of books. It incorporates features such as filtering, sorting, search, authentication, and authorization. The API is backed by a PostgreSQL database and follows best practices for API development.

## Features

- Create a new book
- Retrieve a book by ID
- Update book details
- Delete a book
- List all books with pagination support
- Filter books by title, author, or category
- Sort books by different attributes
- User authentication with JWT (JSON Web Tokens)
- Role-based access control (RBAC)
- Error handling and exception handling
- Unit testing

## Technologies Used

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- JWT
- Docker

## Getting Started

To get started with this project, follow these steps:

1. Clone the repository:

   ```bash
   git clone <repository_url>
   ```


2. Install the dependencies:

   docker build -t my-fastapi-app .
3. Set up the database connection:

   * Configure the database connection in the `database.py` file. Modify the `SQLALCHEMY_DATABASE_URL` variable with your PostgreSQL connection details.
4. Run the database migrations:

   alembic upgrade head
5. Start the FastAPI server:

   uvicorn main:app --reload
6. The API will be accessible at `http://localhost:8000`. You can explore the available endpoints using tools like cURL, Postman, or your web browser.

## Docker

You can also run the application using Docker for a streamlined development experience. Docker provides a containerized environment that includes all the necessary dependencies.

To run the application with Docker, follow these steps:

1. Build the Docker image:

   docker build -t my-fastapi-app .
2. Run the Docker container:

   docker run -d --name fastapi-app -p 8000:8000 my-fastapi-app
3. The API will be accessible at `http://localhost:8000`.

## API Documentation

The API endpoints and their usage are documented using Swagger UI. You can access the API documentation at `http://localhost:8000/docs` or `http://localhost:8000/redoc`.

## Contribution

Contributions are welcome! If you find any issues or want to contribute to the project, feel free to create a pull request.

## License

This project is licensed under the [MIT License](https://chat.openai.com/c/LICENSE).
