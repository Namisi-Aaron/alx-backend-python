# messaging_app

This is a Django-based web application for the messaging_app for ALX ProDev Backend. Follow the steps below to set up and run the project locally using a virtual environment.

## Prerequisites

Make sure you have the following installed:

- Python 3.8+
- pip (Python package installer)

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Namisi-Aaron/alx-backend-python/
cd messaging_app
````

### 2. Create and Activate a Virtual Environment

#### Using `venv` (built-in with Python 3.3+):

```bash
python -m venv venv
source venv/bin/activate      # On Linux or macOS
venv\Scripts\activate         # On Windows
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

---

## Running the Application

### 1. Apply Migrations

```bash
python manage.py migrate
```

### 2. Create a Superuser (optional, for admin access)

```bash
python manage.py createsuperuser
```

### 3. Start the Development Server

```bash
python manage.py runserver
```

The application will be available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Notes

* Always activate the virtual environment before running any project commands.
* If you make changes to the models, run `python manage.py makemigrations` followed by `python manage.py migrate`.
