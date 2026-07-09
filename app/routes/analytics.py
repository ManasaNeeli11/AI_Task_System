from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User, Document, Task, ActivityLog
from app.schemas import AnalyticsResponse


router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


@router.get("/", response_model=AnalyticsResponse)
def get_analytics(
    db: Session = Depends(get_db)
):

    total_users = db.query(User).count()

    total_documents = db.query(Document).count()

    total_tasks = db.query(Task).count()

    total_activity = db.query(ActivityLog).count()


    recent_activity = db.query(
        ActivityLog
    ).order_by(
        ActivityLog.created_at.desc()
    ).limit(5).all()


    return {

        "total_users": total_users,

        "total_documents": total_documents,

        "total_tasks": total_tasks,

        "total_activity": total_activity,

        "recent_activity": [

            {
                "id": activity.id,
                "user_id": activity.user_id,
                "action": activity.action,
                "created_at": activity.created_at
            }

            for activity in recent_activity

        ]

    }