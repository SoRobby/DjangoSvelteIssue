# Backend

Create .env file for local development.
```
# Set if Django is in debug mode. Options are: True or False
DEBUG=True

# Environment in which the backend is running.
# Options are: PRODUCTION, STAGING, DEVELOPMENT_SERVER, and DEVELOPMENT_LCOAL
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