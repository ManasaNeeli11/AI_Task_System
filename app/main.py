from fastapi import FastAPI

from app.database import engine
from fastapi.middleware.cors import CORSMiddleware
from app import models

from app.routes import auth
from app.routes import documents
from app.routes import search
from app.routes import tasks
from app.routes import analytics
from app.routes import activity


# Create database tables
models.Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="AI Task Management System"
)
app.add_middleware(

    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],

)


# Register routes

app.include_router(auth.router)

app.include_router(documents.router)

app.include_router(search.router)

app.include_router(tasks.router)

app.include_router(analytics.router)

app.include_router(activity.router)



@app.get("/")
def home():

    return {
        "message": "Backend Running Successfully"
    }