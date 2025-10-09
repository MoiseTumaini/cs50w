# Django Project Setup and GitHub Actions CI Guide

This guide covers **setting up a Django project locally** with best practices and **creating a GitHub Actions CI pipeline** to test your Django server and client functionality.

---

## Part 1: Installing and Setting Up a Django Project

### Step 1: Install Python

Make sure Python 3 is installed:

```bash
python --version
```

It should be **3.10+** for modern Django.

---

### Step 2: Create a Project Folder

```bash
mkdir ~/Projects/my_django_project
cd ~/Projects/my_django_project
```

---

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

* Creates a folder `venv` containing an isolated Python environment.

---

### Step 4: Activate the Virtual Environment

```bash
source venv/bin/activate   # Linux/macOS
# OR
.\venv\Scripts\activate    # Windows PowerShell
```

Your shell prompt should now show `(venv)`.

---

### Step 5: Install Django

```bash
pip install django
```

Verify installation:

```bash
python -m django --version
```

---

### Step 6: Start a Django Project

```bash
django-admin startproject myproject .
```

* `.` ensures project files go in the current folder.

---

### Step 7: Run the Development Server

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

### Step 8: Create a `requirements.txt`

```bash
pip freeze > requirements.txt
```

* Saves all dependencies.
* Recreate environment later:

```bash
pip install -r requirements.txt
```

---

### Step 9: Version Control with Git

```bash
git init
git add .
git commit -m "Initial Django project setup"
```

Push to GitHub if desired.

---

## Part 2: GitHub Actions CI Pipeline to Test Django

### Step 1: Add a Tests Folder

```bash
mkdir tests
```

Create a test file `tests/test_server.py`:

```python
from django.test import TestCase

class SimpleTest(TestCase):
    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
```

* Tests that your server responds to `/`.

---

### Step 2: Create a GitHub Actions Workflow

Create `.github/workflows/ci.yml`:

```yaml
name: Django CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest

    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_USER: postgres
          POSTGRES_PASSWORD: postgres
          POSTGRES_DB: test_db
        ports:
          - 5432:5432
        options: >-
          --health-cmd "pg_isready -U postgres"
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: 3.11

    - name: Install dependencies
      run: |
        python -m venv venv
        source venv/bin/activate
        pip install -r requirements.txt

    - name: Run Django Tests
      run: |
        source venv/bin/activate
        python manage.py test
```

---

### Step 3: Push and Trigger CI

```bash
git add .github/workflows/ci.yml
git commit -m "Add GitHub Actions CI workflow"
git push origin main
```

* Go to GitHub → Actions tab → see tests run automatically.

---

### Notes / Tips

* **Server and client testing**: Use `self.client.get()` or `self.client.post()` for Django endpoints.
* Consider `pytest-django` for advanced testing.
* Workflow can be extended for linting, coverage, and deployment.

---

### Pro Tips

* Each Django project should have its **own virtual environment**.
* Save dependencies with `pip freeze > requirements.txt`.
* Use GitHub Actions to **automate testing** on every push.

This setup ensures isolated environments, clean dependency management, and continuous integration testing for your Django projects.
