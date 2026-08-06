from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import schemas
from database import SessionLocal

router = APIRouter(tags=["Authentication"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register", response_model=schemas.UserResponse)
def register(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):
    new_user = crud.register_user(db, user)

    if not new_user:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    return new_user


@router.post("/login", response_model=schemas.Token)
def login(
    user: schemas.UserLogin,
    db: Session = Depends(get_db)
):
    token = crud.login_user(
        db,
        user.username,
        user.password
    )

    if not token:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )
    return token