from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base


# ----------------------------
# Roles Table
# ----------------------------
class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    role_name = Column(String(50), unique=True, nullable=False)

    users = relationship("User", back_populates="role")


# ----------------------------
# Users Table
# ----------------------------
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    email = Column(String(100), unique=True, nullable=False)

    password = Column(String(255), nullable=False)


    role_id = Column(Integer, ForeignKey("roles.id"))


    role = relationship(
        "Role",
        back_populates="users"
    )


    tasks = relationship(
        "Task",
        back_populates="user"
    )


    activity_logs = relationship(
        "ActivityLog",
        back_populates="user"
    )


# ----------------------------
# Documents Table
# ----------------------------
class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(255))
    filepath = Column(String(255))
    uploaded_at = Column(DateTime(timezone=True), server_default=func.now())


# ----------------------------
# Tasks Table
# ----------------------------
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(200))
    description = Column(Text)

    status = Column(String(50), default="Pending")

    assigned_to = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="tasks")


# ----------------------------
# Activity Logs Table
# ----------------------------
class ActivityLog(Base):
    __tablename__ = "activity_logs"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    action = Column(
        String(255)
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )


    user = relationship(
        "User",
        back_populates="activity_logs"
    )