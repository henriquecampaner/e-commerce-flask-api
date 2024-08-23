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
   git clone https://github.com/your-username/ecommerce-flask-api.git
   cd ecommerce-flask-api
