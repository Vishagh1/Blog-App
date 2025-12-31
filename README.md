# Django Blog App

A simple blog application built using Django as part of my backend learning journey.

---

## Features
- User registration and login
- User profile with profile picture
- Create, update, and delete blog posts
- View posts by a specific user
- Pagination for blog posts
- Email and Password reset
- Django Admin integration

---

## Tech Stack
- Python
- Django
- SQLite
- HTML, CSS, Bootstrap

---

## Setup Instructions
```bash
git clone https://github.com/Vishagh1/Blog-App.git
cd Blog-App
venv\Scripts\activate    # On Windows
venv/bin/activate    # On macOS/Linux
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
#With Docker
```bash
docker-compose up --build
```