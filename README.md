# Dynamic Portfolio Website Development Using Django

**Web Technologies — Spring 2026 | BS Computer Science Term Project**

A fully **dynamic** personal portfolio website built with Django's **Model–View–Template (MVT)** architecture. All portfolio content (bio, education, skills, experience, projects) is stored in a **SQLite database** and fetched using the **Django ORM**. Nothing is hardcoded inside HTML templates.

---

## Project Structure

```
portfolio_project/          # Main Django project (settings, URLs, home view)
├── bio/                    # Bio / About section app
├── education/              # Education section app
├── skills/                 # Skills section app
├── experience/             # Experience section app
├── projects/               # Projects section app
├── templates/              # Base and home templates
├── static/                 # CSS, JavaScript
│   ├── css/style.css
│   └── js/main.js
├── media/                  # Uploaded profile pictures (created after upload)
├── manage.py
├── requirements.txt
└── README.md
```

Each app contains:
- `models.py` — database tables
- `views.py` — fetch data from database
- `admin.py` — register models in Django Admin
- `urls.py` — URL routing for that section
- `templates/` — HTML section partials

---

## Features

| Section      | Model Fields |
|-------------|--------------|
| **Bio**     | Name, job title, profile picture, professional description |
| **Education** | Degree, institute, start/end year, description |
| **Skills**  | Skill name, category, proficiency level |
| **Experience** | Role, organization, start/end date, description |
| **Projects** | Title, description, technologies, GitHub/demo link |

- Responsive design (mobile, tablet, desktop)
- Django Admin for CRUD operations
- Media upload for profile picture
- Static files for CSS/JS

---

## Setup Instructions (Local Development)

### 1. Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

### 2. Clone or Download the Project

```bash
cd "WEB TECHNOLOGIES PROJECT"
```

### 3. Create Virtual Environment (Recommended)

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run Database Migrations

Migrations create database tables from your models:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Admin Login)

```bash
python manage.py createsuperuser
```

Enter username, email, and password when prompted.

### 7. Run Development Server

```bash
python manage.py runserver
```

Open in browser:
- **Portfolio:** http://127.0.0.1:8000/
- **Admin Panel:** http://127.0.0.1:8000/admin/

### 8. Add Your Portfolio Content

1. Go to **Admin** → **Bio** → Add Bio (upload profile picture)
2. Add **Education**, **Skills**, **Experience**, and **Projects** records
3. Refresh the home page — all sections update automatically from the database

---

## GitHub Upload Instructions

### 1. Initialize Git Repository

```bash
git init
git add .
git commit -m "Initial commit: Dynamic Portfolio Website using Django MVT"
```

### 2. Create GitHub Repository

1. Go to [https://github.com/new](https://github.com/new)
2. Name it e.g. `dynamic-portfolio-django`
3. Do **not** initialize with README (you already have one)
4. Click **Create repository**

### 3. Push to GitHub

```bash
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/dynamic-portfolio-django.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

> **Note:** `db.sqlite3`, `media/`, and `venv/` are in `.gitignore` and will not be uploaded.

---

## Deployment Guide

Your final URL should follow this format:

```
<student_id>.netlify.app
```

Example: if your student ID is `BSCS2026001`, your site would be:

```
https://bscs2026001.netlify.app
```

### Important: Django vs Netlify

**Netlify** is designed for **static websites** (HTML/CSS/JS only). A full **Django** app needs a **Python web server** because it uses a database and server-side rendering.

You have **two deployment options**:

---

### Option A — Full Django Deployment (Recommended for this project)

Use a Python-friendly host so Admin, database, and dynamic content all work:

| Platform | Free Tier | Best For |
|----------|-----------|----------|
| [Render](https://render.com) | Yes | Easiest Django deploy |
| [PythonAnywhere](https://www.pythonanywhere.com) | Yes | Beginner-friendly |
| [Railway](https://railway.app) | Limited free | Quick deploy |

#### Deploy on Render (Step-by-Step)

1. Push your project to GitHub (see above)
2. Sign up at [render.com](https://render.com)
3. Click **New** → **Web Service** → connect your GitHub repo
4. Settings:
   - **Build Command:** `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
   - **Start Command:** `gunicorn portfolio_project.wsgi`
5. Add environment variable: `DJANGO_SETTINGS_MODULE=portfolio_project.settings`
6. For production, set `DEBUG=False` and update `SECRET_KEY` (use Render env vars)
7. Deploy → you get a URL like `https://your-app.onrender.com`

After deploy, create superuser via Render shell:
```bash
python manage.py createsuperuser
```

---

### Option B — Netlify (`<student_id>.netlify.app`)

If your instructor requires a **Netlify URL**, you can:

1. **Deploy a static showcase** (HTML/CSS snapshot) — *loses live Admin/database*
2. **OR** use Netlify only for a **landing page** that links to your live Django site on Render

#### Netlify Static Deploy (for URL requirement only)

1. Sign up at [netlify.com](https://www.netlify.com)
2. Run locally and save your portfolio HTML:
   ```bash
   python manage.py runserver
   # Visit http://127.0.0.1:8000 → Save page as HTML (after adding all data)
   ```
3. In Netlify: **Add new site** → **Deploy manually** → drag a folder with `index.html`, `static/` CSS/JS
4. Go to **Site settings** → **Change site name** → set to your student ID:
   ```
   bscs2026001
   ```
   Your URL becomes: `https://bscs2026001.netlify.app`

> For viva: explain that the **full dynamic project runs on Django + SQLite**, and Netlify static deploy is only if the teacher requires that specific URL format. The **recommended** approach is Render/Railway for true dynamic behavior.

---

## Database Migration Commands (Quick Reference)

| Command | Purpose |
|---------|---------|
| `python manage.py makemigrations` | Create migration files from model changes |
| `python manage.py migrate` | Apply migrations to database |
| `python manage.py createsuperuser` | Create admin login |
| `python manage.py collectstatic` | Collect static files for production |

---

## Viva Preparation — Explain in Simple Words

### 1. What is Django MVT Architecture?

- **Model (M):** Defines database structure (tables and fields). Example: `Bio` model stores name, job title, picture.
- **View (V):** Python functions that fetch data from models and pass it to templates. Example: `home()` view gets all Bio, Education, Skills data.
- **Template (T):** HTML files with Django template tags (`{% for %}`, `{{ variable }}`) that display data dynamically.

**Flow:** User visits URL → **View** queries **Model** (database) → **Template** renders HTML → browser shows page.

### 2. Why Separate Apps?

Each major section (`bio`, `education`, `skills`, `experience`, `projects`) is a **separate Django app** because:
- **Modularity** — each section has its own model, admin, and template
- **Easy maintenance** — change Skills without touching Education code
- **Follows Django best practice** — one app = one feature area
- **Clear for viva** — you can explain each app independently

### 3. How is Data Stored in Models?

Models are Python classes that map to database tables. When you run `migrate`, Django creates tables like `bio_bio`, `education_education`. Each row is one record (e.g., one degree, one skill).

### 4. How Do Views Fetch Data?

Views use **Django ORM** (Object-Relational Mapping):

```python
Bio.objects.first()           # Get bio record
Education.objects.all()       # Get all education records
Skill.objects.all()           # Get all skills
```

No SQL is written manually — Django converts these to database queries.

### 5. How Do Templates Display Data Dynamically?

Templates use Django template language — **no hardcoded portfolio text**:

```django
<h1>{{ bio.name }}</h1>
{% for edu in education_list %}
  <h3>{{ edu.degree }}</h3>
{% endfor %}
```

Data comes from the view's `context` dictionary.

### 6. How is Django Admin Used?

All models are registered in `admin.py`. Superuser logs in at `/admin/` and can **Add**, **Edit**, **Delete** records through a web form. Changes appear on the website immediately — no code changes needed.

### 7. How Does Deployment Work?

- **Development:** `runserver` runs Django locally with SQLite
- **Production:** Code is pushed to GitHub → hosting platform installs `requirements.txt` → runs `migrate` → serves app with **Gunicorn**
- **Static files:** CSS/JS collected via `collectstatic`, served by **WhiteNoise**
- **Media files:** Profile pictures stored in `media/` folder (on free hosts, use cloud storage for production)

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Profile picture not showing | Check `MEDIA_URL` and `MEDIA_ROOT` in settings; ensure file uploaded in Admin |
| `No module named django` | Activate venv and run `pip install -r requirements.txt` |
| Admin CSS broken | Run `python manage.py collectstatic` |
| Empty sections on website | Add data in Django Admin for each model |

---

## Author

Replace with your name and student ID for submission.

**Course:** Web Technologies — Spring 2026  
**Project:** Dynamic Portfolio Website Development Using Django
