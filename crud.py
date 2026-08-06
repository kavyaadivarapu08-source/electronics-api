from sqlalchemy.orm import Session
from security import hash_password, verify_password, create_access_token
import models
import schemas
import models, schemas

def create_laptop(db: Session, laptop: schemas.LaptopCreate):
    db_laptop = models.Laptop(**laptop.model_dump())
    db.add(db_laptop)
    db.commit()
    db.refresh(db_laptop)
    return db_laptop

def get_laptops(db: Session):
    return db.query(models.Laptop).all()

def get_laptop(db: Session, laptop_id: int):
    return db.query(models.Laptop).filter(
        models.Laptop.id == laptop_id
    ).first()

def update_laptop(db: Session, laptop_id: int, laptop: schemas.LaptopCreate):
    db_laptop = get_laptop(db, laptop_id)

    if not db_laptop:
        return None

    db_laptop.brand = laptop.brand
    db_laptop.model = laptop.model
    db_laptop.processor = laptop.processor
    db_laptop.ram = laptop.ram
    db_laptop.price = laptop.price

    db.commit()
    db.refresh(db_laptop)

    return db_laptop

def delete_laptop(db: Session, laptop_id: int):
    db_laptop = get_laptop(db, laptop_id)

    if not db_laptop:
        return None

    db.delete(db_laptop)
    db.commit()

    return db_laptop



    

def register_user(db, user: schemas.UserCreate):
    existing_user = db.query(models.User).filter(
        models.User.username == user.username
    ).first()

    if existing_user:
        return None

    hashed_password = hash_password(user.password)

    new_user = models.User(
        username=user.username,
        email=user.email,
        password=hashed_password,
        role="user"
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def login_user(db, username: str, password: str):
    user = db.query(models.User).filter(
        models.User.username == username
    ).first()

    if not user:
        return None

    if not verify_password(password, user.password):
        return None

    token = create_access_token(
        {
            "sub": user.username,
            "role": user.role
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }