Create a `README.md` file in your project root and paste this content:

```md
# AI Task Management System

An AI-powered Task Management System that helps users manage tasks, upload documents, perform semantic search, and monitor activities through an analytics dashboard.

The system combines **FastAPI backend**, **React frontend**, **MySQL database**, and **AI-based semantic search** to provide an intelligent task management experience.

---

# Features

## Authentication
- User registration and login
- Role-based user management
- Secure password handling

## Document Management
- Upload documents
- Store document details
- Extract document information
- Perform AI-powered semantic search

## Semantic Search
- Search documents using natural language queries
- AI-based similarity matching using embeddings
- Retrieve relevant document results

## Task Management
- Create tasks
- Assign tasks to users
- View assigned tasks
- Track task status

## Analytics Dashboard
- Total documents count
- Total tasks count
- Activity tracking
- Recent user activities

## Activity Logs
- Track user actions
- Store timestamps of activities

---

# Tech Stack

## Backend

- Python
- FastAPI
- SQLAlchemy
- MySQL
- Pydantic
- Sentence Transformers
- Vector Database
- Uvicorn

## Frontend

- React.js
- Vite
- JavaScript
- Axios
- React Router DOM
- CSS

## Database

- MySQL

## Tools

- Git & GitHub
- VS Code
- Postman
- Swagger API Documentation

---

# Project Structure

```

AI_Task_System

│
├── backend
│   │
│   ├── app
│   │   ├── routes
│   │   │   ├── auth.py
│   │   │   ├── documents.py
│   │   │   ├── search.py
│   │   │   ├── tasks.py
│   │   │   ├── analytics.py
│   │   │   └── activity.py
│   │   │
│   │   ├── services
│   │   │   ├── embedding.py
│   │   │   ├── vector_db.py
│   │   │   └── activity_logger.py
│   │   │
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   └── main.py
│   │
│   └── uploads
│
│
└── frontend
│
├── src
│   ├── api
│   ├── components
│   ├── pages
│   ├── App.jsx
│   └── main.jsx
│
├── package.json
└── vite.config.js

````

---

# Installation and Setup

## Clone Repository

```bash
git clone https://github.com/ManasaNeeli11/AI_Task_System.git
````

Move into project folder:

```bash
cd AI_Task_System
```

---

# Backend Setup

Go to backend:

```bash
cd backend
```

Create virtual environment:

```bash
python -m venv myenv
```

Activate environment:

### Windows

```bash
myenv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run FastAPI server:

```bash
uvicorn app.main:app --reload
```

Backend will run at:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

# Frontend Setup

Open another terminal:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start React application:

```bash
npm run dev
```

Frontend will run at:

```
http://localhost:5173
```

---

# API Endpoints

## Authentication

| Method | Endpoint         | Description   |
| ------ | ---------------- | ------------- |
| POST   | `/auth/register` | Register user |
| POST   | `/auth/login`    | Login user    |

---

## Documents

| Method | Endpoint            | Description     |
| ------ | ------------------- | --------------- |
| POST   | `/documents/upload` | Upload document |

---

## Semantic Search

| Method | Endpoint          | Description      |
| ------ | ----------------- | ---------------- |
| GET    | `/search/?query=` | Search documents |

---

## Tasks

| Method | Endpoint  | Description |
| ------ | --------- | ----------- |
| GET    | `/tasks/` | Get tasks   |
| POST   | `/tasks/` | Create task |

---

## Analytics

| Method | Endpoint      | Description    |
| ------ | ------------- | -------------- |
| GET    | `/analytics/` | View analytics |

---

## Activity

| Method | Endpoint     | Description     |
| ------ | ------------ | --------------- |
| GET    | `/activity/` | View activities |

---

<<<<<<< HEAD
# Screenshots

(Add application screenshots here)
=======
## Screenshots

### Login Page

![Login](screenshots/login.png)

### Dashboard

![Dashboard](screenshots/dashboard.png)

### Upload Document

![Upload](screenshots/upload.png)

### Semantic Search

![Search](screenshots/search.png)
>>>>>>> 9a9766a2323cbd82900c554b3ab5a6d37995a368

---

# Future Enhancements

* JWT authentication
* Admin dashboard
* Cloud deployment
* Advanced AI document understanding
* Email notifications
* Real-time task updates

---

# Author

**Manasa Neeli**

GitHub:
[https://github.com/ManasaNeeli11](https://github.com/ManasaNeeli11)

---

# License

This project is developed for learning and demonstration purposes.

````
