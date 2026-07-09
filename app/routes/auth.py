from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User
from app.schemas import UserRegister, UserLogin
from app.auth import hash_password
from app.auth import verify_password
from app.auth import create_access_token

router = APIRouter(prefix="/auth", tags=["Authentication"])
@router.post("/register")
def register(user: UserRegister, db: Session = Depends(get_db)):

    check = db.query(User).filter(
        User.email == user.email
    ).first()

    if check:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    new_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password),
        role_id=user.role_id
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return {
        "message": "User Registered Successfully"
    }
@router.post("/login")
def login(user: UserLogin,
          db: Session = Depends(get_db)):

    db_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid Email"
        )

    if not verify_password(
            user.password,
            db_user.password):

        raise HTTPException(
            status_code=401,
            detail="Invalid Password"
        )

    token = create_access_token(
        {"sub": db_user.email}
    )

    return {

        "access_token": token,

        "token_type": "bearer"

    }