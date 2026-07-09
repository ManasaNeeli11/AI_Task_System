from pydantic import BaseModel
from datetime import datetime


# -------------------------
# Authentication Schemas
# -------------------------

class UserRegister(BaseModel):

    name: str
    email: str
    password: str
    role_id: int



class UserLogin(BaseModel):

    email: str
    password: str



# -------------------------
# Analytics Schemas
# -------------------------

class ActivityResponse(BaseModel):

    id: int
    user_id: int
    action: str
    created_at: datetime



class AnalyticsResponse(BaseModel):

    total_users: int
    total_documents: int
    total_tasks: int
    total_activity: int
    recent_activity: list[ActivityResponse]



# -------------------------
# Task Schemas
# -------------------------

class TaskResponse(BaseModel):

    id: int
    title: str
    description: str
    status: str
    assigned_to: int



# -------------------------
# Document Schemas
# -------------------------

class DocumentResponse(BaseModel):

    id: int
    filename: str
    filepath: str