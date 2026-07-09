from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Task


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.get("/")
def get_tasks(
    db: Session = Depends(get_db)
):

    tasks = db.query(Task).all()

    return tasks


@router.post("/")
def create_task(
    title: str,
    description: str,
    assigned_to: int,
    db: Session = Depends(get_db)
):

    task = Task(
        title=title,
        description=description,
        assigned_to=assigned_to
    )

    db.add(task)
    db.commit()
    db.refresh(task)

    return task