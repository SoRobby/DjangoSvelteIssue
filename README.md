# Project Setup Guide

This guide provides instructions for setting up the backend (Django) and frontend (Svelte/SvelteKit) for the project. Follow these steps to configure and run the application.

---

## Backend (Django)

### 1. Install Required Packages
To install all necessary dependencies for the Django backend, run the following command:

```bash
pip install -r requirements.txt
```

### 2. Configure Environment Variables
Ensure a `.env` file exists in the `/backend/` directory with the following contents:

```ini
# Set if Django is in debug mode. Options are: True or False
DEBUG=True

# Environment in which the backend is running.
# Options are: PRODUCTION, STAGING, DEVELOPMENT_SERVER, and DEVELOPMENT_LOCAL
ENVIRONMENT=DEVELOPMENT_LOCAL

# Frontend root URL (Svelte). Example: localhost:1234
# TODO - change this to FRONTEND_ROOT_DOMAIN
FRONTEND_ROOT_URL=localhost:5173

CORS_ALLOWED_ORIGINS=http://localhost:5173,http://localhost:8000,http://127.0.0.1:8000

# Log level for backend logs
LOG_LEVEL=DEBUG

# Database credentials (Only needed for PRODUCTION, STAGING, and DEVELOPMENT_SERVER environments, NOT NEEDED for DEVELOPMENT_LOCAL)
DATABASE_URL=postgres://user:password@localhost:5432/dbname
DATABASE_NAME=your_db_name
DATABASE_USER=your_db_user
DATABASE_PASSWORD=your_db_password
DATABASE_HOST=your_db_host
DATABASE_PORT=1234
DATABASE_CONN_MAX_AGE=600
```

### 3. Apply Database Migrations
Run the following commands to make migrations and apply them to the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Development Database
An SQLite database should already exist with the following credentials for development:

- **Username:** `admin@admin.com`
- **Password:** `admin`

---

## Frontend (Svelte / SvelteKit)

### 1. Install Node Modules
Navigate to the `/frontend/` directory and install the required dependencies:

```bash
npm install
```

### 2. Configure Environment Variables
Ensure a `.env` file exists in the `/frontend/` directory with the following contents:

```ini
# Private
SECRET_KEY=my_secret_key

# Public
PUBLIC_API_ROOT_URL=http://localhost:8000
PUBLIC_SITE_NAME=Company Name
```

---

### Notes
- For production, staging, and server environments, ensure the `.env` files contain accurate configurations for their respective environments.
- Update the `FRONTEND_ROOT_URL` in the backend `.env` file to the actual frontend domain when deploying.

Feel free to reach out if you encounter any issues during setup!