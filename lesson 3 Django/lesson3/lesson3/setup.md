# 🚀 Django Project Setup Guide

This guide explains how to set up and run the Django project on any new machine.

---

## 1. Clone the Repository
```sh
git clone <your-repo-url>
cd <your-repo-folder>
# 1) Create virtual environment
python -m venv venv

# 2) Activate it
# Linux / macOS
source venv/bin/activate
# Windows (PowerShell)
.\venv\Scripts\activate

# 3) Install dependencies
pip install -r requirements.txt
# (If requirements.txt does not exist yet, run instead:)
# pip install django
# pip freeze > requirements.txt

# 4) Apply database migrations
python manage.py migrate

# 5) Create superuser (for admin access)
python manage.py createsuperuser

# 6) Run the development server
python manage.py runserver

# Python
__pycache__/
*.py[cod]
*.sqlite3

# Virtual environments
venv/
.env/

# IDE / Editor
.vscode/
.idea/
