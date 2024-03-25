# Online Store Django Rest API

This is a Django Rest API managing Online Store.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/CHAKHVA/online-store.git
```

2. Navigate into the project directory

```bash
cd online-store
```

2. Set up a virtual environment (optional):

```bash
# Windows
python -m venv .venv
# macOS/Linux
python3 -m venv .venv

# Activate it on Windows
.venv\Scripts\activate
# Or on MacOS/Linux
source .venv/bin/activate
```

3. Install the dependencies:

```bash
# Windows
pip install -r requirements.txt
# MacOS/Linux
pip3 install -r requirements.txt
```

## Configuration

-   Change database configuration in `onlinestore/onlinestore/settings.py`

## Usage

1. Make migrations

```bash
python manage.py makemigrations
```

2. Migrate models

```bash
python manage.py migrate
```

3. Create Superuser

```bash
python manage.py createsuperuser
```

4. Seed initial data

```bash
python manage.py loaddata initial_data.json
```

5. Run Application

```bash
python manage.py runserver
```

## API Endpoints

### Authentication

1. `/auth/register/`
    - POST: Registers user and returns access token
2. `/auth/login/`
    - POST: Logins user and returns access token

### Products

1. `/products-list/`
    - GET: Lists all products.
2. `/products/`
    - POST: Creates a new product.
3. `/products/<product_id>/`
    - GET: Retrieves details of a single product (including change history).
    - PUT: Updates a product.
    - DELETE: Deletes a product.

### Categories

1. `/categories/`
    - GET: Lists all categories (includes product count per category).
    - POST: Creates a new category.
2. `/categories/<category_id>/`
    - GET: Retrieves details of a single category (includes product count per category).
    - PUT: Updates a category.
    - DELETE: Deletes a category.
