# Containerizing a basic FastAPI Student Management Application integrating it with PostgreSQL
## Technologies we'd be using 
* FastAPI
* Docker compose 
* Dev containers
* PostgreSQL

This project is a basic FastAPI running application inside a Docker container  that performs CRUD (Create, Read, Update, Delete) operations for managing student data. The data includes student names, emails, and zip codes. The application is integrated with a PostgreSQL database.

## Features

- **Create a new student**: Add a new student to the database.
- **Read student data**: Retrieve student data by ID.
- **Update student data**: Update the details of an existing student.
- **Delete a student**: Remove a student from the database.

## Technologies Used

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.6+.
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **PostgreSQL**: A powerful, open source object-relational database system.
- **Pydantic**: Data validation and settings management using Python type annotations.

## Prerequisites

- Python 3.7+
- PostgreSQL database

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/fastapi-student-management.git
   cd fastapi-student-management










### To dive deep into logs of a specific service 
```docker compose logs <service name>
```

```docker exec -it SQLcontainer psql -U postgres -d postgres
```
