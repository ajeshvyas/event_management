# This is a Django REST Framework (DRF) project for an Event Management API. It provides endpoints for managing events and tickets. The API documentation is available through Swagger UI and ReDoc.

# Requirements

- Python 3.x
- Django 3.2
- Django REST Framework 3.14.0
- psycopg2-binary 2.9.6
- wheel
- drf-yasg 1.21.5
- Faker 18.10.1

# Setup :

    - Clone the repository:

        `git clone <repository-url>`
        `cd event_management`
        Create and activate a virtual environment (optional but recommended):

        `python3 -m venv venv`
        `source venv/bin/activate`

    - Install the required packages:

        `pip install -r requirements.txt`

    - Set up the database:

        Update the DATABASES configuration in settings.py to match your PostgreSQL database settings.

        `DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'your_database_name',
                'USER': 'your_database_user',
                'PASSWORD': 'your_database_password',
                'HOST': 'your_database_host',
                'PORT': 'your_database_port',
            }
        }`

    - Apply the database migrations:

        `python manage.py migrate`

    - Create a superuser (admin) account:

        `python manage.py createsuperuser`
        Follow the prompts to set a username and password for the admin account.

    - Start the development server:

        `python manage.py runserver`

    - The API will be accessible at http://localhost:8000/.

# API Endpoints :

    - Event Management API: http://localhost:8000/api/events/
    - User Registration: http://localhost:8000/api/users/register/
    - User Login: http://localhost:8000/api/users/login/
    - API Documentation
    - Swagger UI: http://localhost:8000/api/swagger/
    - ReDoc: http://localhost:8000/api/redoc/

# Admin Interface

    The Django admin interface is available at http://localhost:8000/admin/. Use the superuser account created in step 6 to access the admin dashboard.

# Testing
    
    To run the tests, use the following command:
    
    `python manage.py test`