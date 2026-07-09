from app.models import ActivityLog


def log_activity(
        db,
        user_id,
        action
):

    activity = ActivityLog(
        user_id=user_id,
        action=action
    )

    db.add(activity)
    db.commit()

    return activity