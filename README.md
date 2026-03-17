![Python](https://img.shields.io/badge/python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-async-green)
![Status](https://img.shields.io/badge/status-live-success)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)

# 🚀 MediaHub — Fullstack Media Sharing App

A simple yet **production-ready fullstack media sharing platform** built with FastAPI, PostgreSQL, and Streamlit.

Users can register, login, upload media, and manage posts — all deployed live with real-world architecture.

---

## 🌍 Live Demo

- 🔗 Frontend: https://media-fastapi.streamlit.app  
- 🔗 Backend API: https://mediahub-fastapi-production.up.railway.app/docs  

---

## ⚡ Features

- 🔐 JWT Authentication (Register & Login)
- 📸 Upload Images & Videos
- 🧾 Public Feed (latest posts)
- 🗑️ Delete your own posts
- ☁️ Cloud media storage (ImageKit)
- ⚡ Async FastAPI backend
- 🧪 End-to-End API Testing (pytest)
- 🌍 Fully deployed (Railway + Streamlit)

---

## 🛠️ Tech Stack

### Backend
- ⚡ FastAPI
- 🗄️ PostgreSQL (Railway)
- 🔑 FastAPI Users (JWT Auth)
- 🧠 SQLAlchemy (Async ORM)

### Frontend
- 🎨 Streamlit

### Testing
- 🧪 Pytest
- 🔁 End-to-End API Flow Testing (Auth + Protected Routes)

### Cloud & Deployment
- 🚂 Railway (Backend + Database)
- 🌐 Streamlit Cloud (Frontend)
- ☁️ ImageKit (Media CDN)

---

## 🧠 Architecture Overview

Client (Streamlit)  
⬇  
FastAPI Backend (Railway)  
⬇  
PostgreSQL Database  
⬇  
ImageKit (Media CDN)

---

## 🚀 How to Run Locally

```bash
git clone https://github.com/ricothenfx/mediahub-fastapi.git
cd mediahub-fastapi
```

### 1. Setup environment

```bash
cp .env.example .env
```

Edit `.env`:

```env
# Local development (SQLite)
DATABASE_URL=sqlite+aiosqlite:///./test.db

# Production (PostgreSQL - Railway)
# DATABASE_URL=postgresql+asyncpg://user:password@host:port/dbname

API_URL=http://localhost:8000
```

---

### 2. Install dependencies

```bash
uv sync
```

---

### 3. Run backend

```bash
uv run start.py
```

---

### 4. Run frontend

```bash
uv run streamlit run frontend.py
```

---

## 🧪 Testing

Run all tests:

```bash
pytest
```

Includes:

- User registration test
- Login & JWT authentication test
- Protected route access test
- Full end-to-end flow test

---

## 🎯 Why This Project?

This project demonstrates:

- Building a **real-world fullstack application**
- Implementing **authentication & authorization**
- Working with **async backend architecture**
- Using **PostgreSQL in production**
- Writing **end-to-end API tests**
- Deploying a complete system to the cloud

---

## 👨‍💻 Author

**Rico**  
GitHub: https://github.com/ricothenfx

---

## ⭐ Notes

This project is intentionally simple but designed to reflect **real-world backend architecture, testing practices, and deployment workflow**.
