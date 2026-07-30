from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import crud
import schemas
import models

from database import Base, engine, SessionLocal

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/laptops", response_model=schemas.LaptopResponse)
def create_laptop(
    laptop: schemas.LaptopCreate,
    db: Session = Depends(get_db)
):
    return crud.create_laptop(db, laptop)


@app.get("/laptops", response_model=List[schemas.LaptopResponse])
def get_laptops(db: Session = Depends(get_db)):
    return crud.get_laptops(db)


@app.put("/laptops/{laptop_id}", response_model=schemas.LaptopResponse)
def update_laptop(
    laptop_id: int,
    laptop: schemas.LaptopCreate,
    db: Session = Depends(get_db)
):
    updated = crud.update_laptop(db, laptop_id, laptop)
    if not updated:
        raise HTTPException(status_code=404, detail="Laptop not found")
    return updated


@app.delete("/laptops/{laptop_id}")
def delete_laptop(
    laptop_id: int,
    db: Session = Depends(get_db)
):
    deleted = crud.delete_laptop(db, laptop_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Laptop not found")
    return {"message": "Laptop deleted successfully"}


@app.post("/mobiles", response_model=schemas.MobileResponse)
def create_mobile(
    mobile: schemas.MobileCreate,
    db: Session = Depends(get_db)
):
    return crud.create_mobile(db, mobile)


@app.get("/mobiles", response_model=List[schemas.MobileResponse])
def get_Mobile(db: Session = Depends(get_db)):
    return crud.get_Mobile(db)

@app.put("/Mobile/{Mobile_id}", response_model=schemas.MobileResponse)
def update_Mobile(
    laptop_id: int,
    laptop: schemas.MobileCreate,
    db: Session = Depends(get_db)
):
    updated = crud.update_Mobile(db, Mobile_id, Mobile)
    if not updated:
        raise HTTPException(status_code=404, detail="Mobile not found")
    return updated


@app.delete("/Mobile/{Mobile_id}")
def delete_Mobile(
    Mobile_id_id: int,
    db: Session = Depends(get_db)
):
    deleted = crud.delete_Mobile(db, Mobile_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Mobile not found")
    return {"message": "Mobile deleted successfully"}



@app.post("/watch", response_model=schemas.WatchResponse)
def create_watch(
    watch: schemas.WatchCreate,
    db: Session = Depends(get_db)
):
    return crud.create_watch(db, watch)



@app.get("/watch", response_model=List[schemas.WatchResponse])
def get_watch(db: Session = Depends(get_db)):
    return crud.get_watch(db)


@app.put("/watch/{watch_id}", response_model=schemas.WatchResponse)
def update_watch(
    watch_id: int,
    watch: schemas.WatchCreate,
    db: Session = Depends(get_db)
):
    updated = crud.update_watch(db, watch_id, watch)
    if not updated:
        raise HTTPException(status_code=404, detail="Watch not found")
    return updated


@app.delete("/watch/{watch_id}")
def delete_watch(
    watch_id: int,
    db: Session = Depends(get_db)
):
    deleted = crud.delete_watch(db, watch_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Watch not found")
    return {"message": "Watch deleted successfully"}


@app.post("/tv", response_model=schemas.TVResponse)
def create_tv(
    tv: schemas.TVCreate,
    db: Session = Depends(get_db)
):
    return crud.create_tv(db, tv)


@app.get("/tv", response_model=List[schemas.TVResponse])
def get_tv(db: Session = Depends(get_db)):
    return crud.get_tv(db)


@app.get("/tv/{tv_id}", response_model=schemas.TVResponse)
def get_one_tv(
    tv_id: int,
    db: Session = Depends(get_db)
):
    tv = crud.get_one_tv(db, tv_id)
    if not tv:
        raise HTTPException(status_code=404, detail="TV not found")
    return tv


@app.put("/tv/{tv_id}", response_model=schemas.TVResponse)
def update_tv(
    tv_id: int,
    tv: schemas.TVCreate,
    db: Session = Depends(get_db)
):
    updated = crud.update_tv(db, tv_id, tv)
    if not updated:
        raise HTTPException(status_code=404, detail="TV not found")
    return updated


@app.delete("/tv/{tv_id}")
def delete_tv(
    tv_id: int,
    db: Session = Depends(get_db)
):
    deleted = crud.delete_tv(db, tv_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="TV not found")
    return {"message": "TV deleted successfully"}





@app.post("/headphones", response_model=schemas.HeadphoneResponse)
def create_headphone(
    headphone: schemas.HeadphoneCreate,
    db: Session = Depends(get_db)
):
    return crud.create_headphone(db, headphone)


@app.get("/headphones", response_model=List[schemas.HeadphoneResponse])
def get_one_headphones(db: Session = Depends(get_db)):
    return crud.get_one_headphones(db)


@app.get("/headphones/{headphone_id}", response_model=schemas.HeadphoneResponse)
def get_one_headphones(
    headphone_id: int,
    db: Session = Depends(get_db)
):
    headphones = crud.get_one_headphones(db, headphones_id)
    if not headphones:
        raise HTTPException(status_code=404, detail="headphones not found")
    return headphones

@app.put("/headphones/{headphone_id}", response_model=schemas.HeadphoneResponse)
def update_headphones(
    headphones_id: int,
    headphones: schemas.HeadphoneCreate,
    db: Session = Depends(get_db)
):
    updated = crud.update_headphones(db, headphones_id, headphones)
    if not updated:
        raise HTTPException(status_code=404, detail="headphones not found")
    return updated


@app.delete("/headphones/{headphones_id}")
def delete_headphones(
    headphones_id: int,
    db: Session = Depends(get_db)
):
    deleted = crud.delete_headphones(db, headphones_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="headphones not found")
    return {"message": "headphones deleted successfully"}