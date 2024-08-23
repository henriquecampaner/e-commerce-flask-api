# E-commerce Flask API

This repository contains a simple e-commerce backend API built using Flask, Flask-Login for user authentication, Flask-CORS to handle Cross-Origin Resource Sharing, and Flask-SQLAlchemy as the ORM to interact with the database. The API allows users to register, log in, manage their cart, and perform CRUD operations on products.

## Features

- **User Authentication**: Users can log in and log out using sessions.
- **Product Management**: Allows CRUD operations (Create, Read, Update, Delete) on products.
- **Shopping Cart**: Users can add products to their cart, view their cart, remove items, and proceed to checkout.
- **RESTful API Endpoints**: API endpoints for handling user authentication, product management, and cart management.
- **Database**: SQLite is used as the database for storing users, products, and cart items.

## Technologies Used

- **Flask**: Python web framework for building the API.
- **Flask-Login**: To manage user sessions and authentication.
- **Flask-CORS**: To handle Cross-Origin Resource Sharing, allowing the API to be accessed from different domains.
- **Flask-SQLAlchemy**: SQLAlchemy integration for Flask to manage database interactions.
- **SQLite**: Database used for persistence.

## Installation

### Prerequisites

- Python 3.6 or higher installed.
- A virtual environment tool like `venv` or `virtualenv`.

### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/henriquecampaner/e-commerce-flask-api.git
   cd e-commerce-flask-api

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the database:**

   Start a Python shell within the project and run the following commands to create the database:

   ```python
   from app import db
   db.create_all()
   exit()
   ```

5. **Run the Flask application:**

   ```bash
   flask run
   ```

   The application will be running on `http://127.0.0.1:5000/` by default.

## API Endpoints

### Authentication

- **POST /login**: Log in a user.
- **POST /logout**: Log out the current user.

### Products

- **GET /api/products**: Retrieve a list of all products.
- **GET /api/products/<int:product_id>**: Retrieve details of a specific product.
- **POST /api/products/add**: Add a new product (Requires login).
- **PUT /api/products/update/<int:product_id>**: Update an existing product (Requires login).
- **DELETE /api/products/delete/<int:product_id>**: Delete a product (Requires login).

### Cart Management

- **POST /api/cart/add/<int:product_id>**: Add a product to the cart (Requires login).
- **DELETE /api/cart/remove/<int:product_id>**: Remove a product from the cart (Requires login).
- **GET /api/cart**: View the current user's cart (Requires login).
- **POST /api/cart/checkout**: Checkout and clear the cart (Requires login).

