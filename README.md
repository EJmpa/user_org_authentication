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


## API Endpoints
### Authentication
* POST /auth/register: Register a new user
* POST /auth/login: Login a user and obtain a JWT token

### Users
* GET /api/users: Get a list of all users
* GET /api/users/:id: Get a user by ID
* PUT /api/users/:id: Update a user `(Yet to be implemented)`
* DELETE /api/users/:id: Delete a user `(Yet to be implemented)`

### Organisations
* GET /api/organisations: Get a list of all organisations
* GET /api/organisations/:id: Get an organisation by ID
* POST /api/organisations: Create a new organisation
* PUT /api/organisations/:id: Update an organisation `(Yet to be implemented)`
* DELETE /api/organisations/:id: Delete an organisation `(Yet to be implemented)`

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing
Contributions are welcome! If you’d like to contribute to this project, please fork the repository and submit a pull request.

## Support
If you encounter any issues or have any questions, please open an issue on the repository.

## Authors
Chukwuemeka Jude Chukwu\
chukwuemekajc@gmail.com

## Version History
0.1: Initial Release

## Acknowledgments
HNG (Organisation orgabising the internship)\
Flask\
Flask-JWT-Extended\
Flask-Migrate\
Flask-Marshmallow\
Bcrypt
