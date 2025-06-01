# ALX Travel App

## Project Overview

The ALX Travel App is a Django-based application designed to serve as a robust travel listing platform. The project follows best practices in backend setup, database integration, API documentation, and version control. This project is part of the ALX program and aims to provide hands-on experience in building scalable web applications using Django and MySQL.

### Key Features

* Django backend with RESTful API design
* MySQL database integration for reliable data storage
* Automated API documentation using Swagger (drf-yasg)
* Version control with Git and GitHub for collaborative development
* Modular project structure following Django best practices

---

## Technologies Used

* Python 3.13
* Django 5.2.1
* Django REST Framework
* MySQL 8.0.42
* drf-yasg (Swagger API documentation)
* django-environ (Environment variable management)
* Celery and RabbitMQ (for background task processing)
* Git & GitHub for version control

---

## Project Structure

```bash
alx_travel_app/
├── manage.py
├── env/
├── README.md
├── .env
└── alx_travel_app/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── wsgi.py
    ├── asgi.py
    └── listings/
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── models.py
        ├── views.py
        ├── urls.py
        └── migrations/
```

---

## Setup Instructions

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/alx_travel_app.git
cd alx_travel_app
```

### Step 2: Set Up the Virtual Environment

```bash
pip install virtualenv
virtualenv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r alx_travel_app/requirement.txt
```

### Step 4: Database Configuration

1. Install MySQL.
2. Create a database:

```sql
CREATE DATABASE alxtravelapp;
CREATE USER 'alxuser'@'localhost' IDENTIFIED BY 'securepassword';
GRANT ALL PRIVILEGES ON alxtravelapp.* TO 'alxuser'@'localhost';
FLUSH PRIVILEGES;
```

### Step 5: Update Environment Variables

```bash
touch alx_travel_app/.env
```

Add the following:

```env
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_NAME=your_database_name
DATABASE_USER=your_database_user
DATABASE_PASSWORD=securepassword
DATABASE_HOST=127.0.0.1
DATABASE_PORT=3306
```

### Step 6: Run Migrations

```bash
python manage.py migrate
```

### Step 7: Create Superuser

```bash
python manage.py createsuperuser
```

### Step 8: Start the Server

```bash
python manage.py runserver
```

Access at: `http://127.0.0.1:8000/admin/`

---

## API Documentation

Swagger is integrated for automated API documentation. Access it at:

```url
http://127.0.0.1:8000/swagger/
```

Example Endpoint:

* **Hello World Endpoint:**

  * URL: `/api/listings/hello/`
  * Method: GET
  * Response: `{"message": "Hello, ALX Travel App!"}`

---

## Version Control

The project is managed using Git.

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/alx_travel_app.git
git push -u origin main
```

---
