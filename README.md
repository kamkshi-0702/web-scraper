# Web Scraping + FastAPI CRUD Application

## 📌 Project Overview

This project demonstrates a complete backend workflow that includes:

* Data extraction from GitHub API
* Data storage using SQLite
* FastAPI-based CRUD operations
* Modular and clean project structure

---

## ⚙️ Tech Stack

* Python 3.x
* FastAPI
* SQLAlchemy
* SQLite
* Requests
* Uvicorn
* Pydantic

---

## 📁 Project Structure

```
web-scraper-fastapi/
│
├── app/
│   ├── main.py          # FastAPI entry point
│   ├── database.py      # Database connection
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic schemas
│   ├── crud.py          # CRUD operations
│   ├── scraper.py       # Data scraping logic
│   ├── config.py        # Environment variables
│   └── __init__.py
│
├── requirements.txt
├── README.md
├── .env
└── .gitignore
```

---

## 🚀 Setup Instructions

### 1. Clone the repository

```
git clone <your-repo-link>
cd web-scraper-fastapi
```

### 2. Create virtual environment

```
python -m venv venv
```

### 3. Activate environment

**Windows (PowerShell):**

```
.\venv\Scripts\Activate.ps1
```

---

### 4. Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### Step 1: Run the scraper

```
python -m app.scraper
```

This will:

* Fetch data from GitHub API
* Store it in SQLite database (`test.db`)

---

### Step 2: Start FastAPI server

```
uvicorn app.main:app --reload
```

---

### Step 3: Access API Docs

Open in browser:

```
http://127.0.0.1:8000/docs
```

---

## 📡 API Endpoints

| Method | Endpoint               | Description    |
| ------ | ---------------------- | -------------- |
| GET    | /items                 | Get all users  |
| GET    | /items/{id}            | Get user by ID |
| GET    | /items/filter?name=abc | Filter users   |
| POST   | /items                 | Create user    |
| PUT    | /items/{id}            | Update user    |
| DELETE | /items/{id}            | Delete user    |

---

## ⚠️ Notes

* A 1-second delay was added between requests to reduce the chances of hitting GitHub API rate limits and ensure smoother execution.
* Duplicate users are avoided using unique constraints
* Environment variables are managed using `.env`

---

## ✅ Features

* Modular architecture
* Pagination support
* Error handling
* Clean API design
* SQLite integration

---

## 📦 Deliverables

* Complete backend system
* Scraper + Database + API
* Fully functional CRUD endpoints

---

## 👨‍💻 Author

Kamakshi Chinta
