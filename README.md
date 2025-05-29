# 🎬 MovieTrack API

MovieTrack is a full-featured backend API for a movie management application where users can organize their personal movie wishlists and watched lists. Built with Django and Django REST Framework, it provides JWT-based authentication and RESTful endpoints to manage movies securely.

---

## 🚀 Tech Stack

- **Backend:** Django, Django REST Framework (DRF)
- **Database:** PostgreSQL
- **Authentication:** JWT (Simple JWT)
- **API Testing:** Postman / Swagger UI (optional)

---

## 🛠 Features

- ✅ User registration and login with JWT
- 🔐 Authenticated access to movie records
- 📝 Add/edit/delete movie entries
- ⭐ Rate and review watched movies
- 📅 Track watched date
- 🎯 Manage wishlist vs watched list
- 📂 Clean RESTful API structure
- 🛡️ Secure user-specific access to movies

---

## 🗃️ Database Schema

### 👤 User Table (extends Django's `AbstractUser`)
| Field       | Type        | Description              |
|-------------|-------------|--------------------------|
| id          | SERIAL      | Primary key              |
| username    | VARCHAR     | Unique username          |
| email       | VARCHAR     | Email address            |
| password    | VARCHAR     | Encrypted password       |
| created_at  | TIMESTAMP   | Timestamp of creation    |

### 🎥 Movie Table
| Field         | Type        | Description                        |
|---------------|-------------|------------------------------------|
| id            | SERIAL      | Primary key                        |
| title         | VARCHAR     | Title of the movie                 |
| year          | INTEGER     | Release year                       |
| genre         | VARCHAR     | Genre of the movie                 |
| status        | VARCHAR     | "Wishlist" or "Watched"            |
| rating        | INTEGER     | Rating (1–5 stars, nullable)       |
| review        | TEXT        | Optional personal review           |
| watched_date  | DATE        | Optional date watched              |
| user          | FK(User)    | Owner of the movie                 |
| created_at    | TIMESTAMP   | Creation timestamp                 |
| updated_at    | TIMESTAMP   | Last update timestamp              |

---

## 🔐 Authentication

JWT-based via **Simple JWT**

- `POST /api/auth/register/` – Register new user
- `POST /api/auth/login/` – Obtain access and refresh tokens
- `POST /api/auth/refresh/` – Refresh access token

---

## 🎬 Movie Endpoints

| Endpoint                  | Method | Description                     |
|--------------------------|--------|---------------------------------|
| `/api/movies/`           | GET    | Get all movies (wishlist + watched) |
| `/api/movies/`           | POST   | Add a new movie                 |
| `/api/movies/{id}/`      | GET    | Get details of a specific movie |
| `/api/movies/{id}/`      | PUT    | Update movie details            |
| `/api/movies/{id}/`      | DELETE | Delete a movie                  |

> 🔒 All movie routes are protected – require JWT.

---

## ⚙️ Setup Instructions

### 1. Clone the Repo
```bash
git clone https://github.com/dhawal1399-ui/movie-track-api.git
cd movie-track-api


Create & Activate Virtual Environment

    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Requirements
    pip install -r requirements.txt



Configure PostgreSQL Database


    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'movietrack',
            'USER': 'postgres',
            'PASSWORD': '1234',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }


Run Migrations

    python manage.py makemigrations
    python manage.py migrate


Start Server

    python manage.py runserver


Sample API Testing (Postman)

   1. Register a user → /api/auth/register/

    2. Login → receive access + refresh tokens

    3. Use the Authorization: Bearer <access_token> header to access movie APIs


Environment Variables Sample (.env.sample)

    DEBUG=True

    DB_NAME=movietrack
    DB_USER=postgres
    DB_PASSWORD=1234
    DB_HOST=localhost
    DB_PORT=5432


Project Structure


    movie-track-api/
    ├── api/
    │   ├── migrations/
    │   ├── __init__.py
    │   ├── models.py
    │   ├── serializers.py
    │   ├── views.py
    │   └── urls.py
    ├── movietrack/
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── manage.py
    └── requirements.txt






