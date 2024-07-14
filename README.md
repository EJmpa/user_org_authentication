# User Organisation Authentication

A Flask-based API for user organisation authentication

## Overview

This repository contains a Flask API that provides user organisation authentication functionality. The API uses JWT (JSON Web Tokens) for authentication and authorisation, and supports user registration, login, and organisation management.

## Features

- User registration with password hashing using Bcrypt
- User login with JWT authentication
- Organisation management (create, read, update, delete)
- User management (create, read, update, delete)
- API endpoints for authentication and authorisation

## Technical Requirements

- Python 3.7+
- Flask 2.0+
- Flask-JWT-Extended 3.25+
- Flask-Migrate 2.5+
- Flask-Marshmallow 0.13+
- Bcrypt 3.2+

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/user_org_authentication.git

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt

3. Create a new database and update the `config.py` file with the database credentials.

4. Run the migrations:
    ```bash
    flask db upgrade

5. Start the API:
    ```bash
    python3 app.py

6. Use a tool like Postman or cURL to test the API endpoints.
