# Local Service Finder

Local Service Finder is a Django portfolio project where users can browse approved local service listings, filter by category and city, and submit new listings for admin approval.

## Features

- Home page with featured categories and recent listings
- Service list page with keyword search, category filter, city filter, and pagination
- Service detail page with provider contact details
- Add-service form built with Django `ModelForm`
- Admin dashboard for approving and managing services
- MySQL-ready configuration with a SQLite fallback for quick local setup

## Tech Stack

- Django
- PyMySQL
- HTML, CSS, Tailwind CSS
- MySQL or SQLite for development fallback

## Project Structure

- `local_service_finder/` project settings and root URLs
- `services/` application logic, models, forms, views, and admin
- `templates/` shared and app templates
- `static/css/` custom styling

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run migrations:

```bash
python manage.py migrate
```

4. Create an admin user:

```bash
python manage.py createsuperuser
```

5. Start the development server:

```bash
python manage.py runserver
```

6. Optional: load sample data for a faster demo:

```bash
python manage.py loaddata services/fixtures/sample_services.json
```

## MySQL Configuration

If you want to use MySQL instead of SQLite, set these environment variables before running the project:

- `MYSQL_DATABASE`
- `MYSQL_USER`
- `MYSQL_PASSWORD`
- `MYSQL_HOST`
- `MYSQL_PORT`

Example values are included in `.env.example`.
