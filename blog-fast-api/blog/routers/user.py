from fastapi import APIRouter, Depends, status, HTTPException
from .. import models, schemas
from ..hashing import Hash

from typing import List
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    old_user = db.query(models.User).filter(models.User.email == request.email).first()
    if old_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'{request.email} already Exist')

    new_user = models.User(name=request.name,
                           email=request.email,
                           password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get('/', response_model=List[schemas.ShowUser])
def show_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def show_user(id:int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} Not found')

    return user
