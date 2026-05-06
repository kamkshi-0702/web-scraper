from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal, engine
from app import models, crud, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Web Scraper CRUD API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/items", response_model=list[schemas.UserResponse])
def get_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_users(db, skip, limit)

@app.get("/items/{user_id}", response_model=schemas.UserResponse)
def get_one(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/items/filter")
def filter_users(name: str, db: Session = Depends(get_db)):
    return crud.filter_users(db, name)

@app.post("/items", response_model=schemas.UserResponse, status_code=201)
def create(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@app.put("/items/{user_id}", response_model=schemas.UserResponse)
def update(user_id: int, user: schemas.UserBase, db: Session = Depends(get_db)):
    updated = crud.update_user(db, user_id, user)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated

@app.delete("/items/{user_id}")
def delete(user_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_user(db, user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "Deleted successfully"}