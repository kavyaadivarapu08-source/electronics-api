from sqlalchemy.orm import Session
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