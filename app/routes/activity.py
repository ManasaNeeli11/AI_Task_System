from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import ActivityLog
from app.schemas import ActivityResponse


router = APIRouter(
    prefix="/activity",
    tags=["Activity"]
)


@router.get("/", response_model=list[ActivityResponse])
def get_activity(
    db: Session = Depends(get_db)
):

    activities = db.query(
        ActivityLog
    ).order_by(
        ActivityLog.created_at.desc()
    ).all()


    return [

        {
            "id": activity.id,
            "user_id": activity.user_id,
            "action": activity.action,
            "created_at": activity.created_at
        }

        for activity in activities

    ]