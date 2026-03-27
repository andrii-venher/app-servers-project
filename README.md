# Local Library (Django)

A small Django 5 project with a `catalog` app. The site root redirects to the catalog home page.

## Prerequisites

- Python 3.10 or newer (3.12 recommended)

## Setup and run

1. **Create and activate a virtual environment** (from the project root):

   ```bash
   python3 -m venv env
   source env/bin/activate    # Windows: env\Scripts\activate
   ```

2. **Install Django** (this project targets Django 5.1):

   ```bash
   pip install "Django>=5.1,<6"
   ```

3. **Apply database migrations** (creates `db.sqlite3` if it does not exist):

   ```bash
   python manage.py migrate
   ```

4. **Start the development server**:

   ```bash
   python manage.py runserver
   ```

5. Open a browser:

   - **Catalog:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/) — redirects to `/catalog/`
   - **Admin:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) — sign in with the superuser account (see below)

Stop the server with `Ctrl+C`. Deactivate the virtual environment with `deactivate` when you are done.

## Django admin: create a superuser

You need a superuser account to log into `/admin/`. Run this **after** migrations, with the virtual environment active and **before or after** starting `runserver` (the server does not need to be running for this command):

```bash
python manage.py createsuperuser
```

Django will prompt you for:

- **Username** — what you type when logging into the admin (can be changed later in the admin).
- **Email address** — optional; press Enter to skip.
- **Password** — enter it twice; Django will reject passwords that are too short or too similar to the username.

Then open [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/), enter that username and password, and you will have full access to the admin site.

To add another admin user later, run `python manage.py createsuperuser` again.
