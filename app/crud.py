from sqlalchemy.orm import Session
from app import models

def get_users(db: Session, skip=0, limit=10):
    return db.query(models.User).offset(skip).limit(limit).all()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_user(db: Session, user):
    existing = db.query(models.User).filter(models.User.id == user.id).first()
    if existing:
        return existing

    db_user = models.User(
        id=user.id,
        login=user.login,
        url=user.url,
        type=user.type
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user_data):
    user = get_user(db, user_id)
    if not user:
        return None

    for key, value in user_data.dict().items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, user_id: int):
    user = get_user(db, user_id)
    if not user:
        return None

    db.delete(user)
    db.commit()
    return user

def filter_users(db: Session, name: str):
    return db.query(models.User).filter(models.User.login.contains(name)).all()