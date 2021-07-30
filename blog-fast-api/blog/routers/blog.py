from fastapi import APIRouter, Depends, status, HTTPException
from .. import models, schemas, oauth2
from typing import List
from sqlalchemy.orm import Session
from ..database import get_db
from ..oauth2 import get_current_user


router = APIRouter(
    prefix="/blog",
    tags=["Blogs"]
)


@router.get('/', response_model=List[schemas.ShowBlog])
def show_blogs(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    blogs = db.query(models.Blog).all()
    return blogs


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog,
                db: Session = Depends(get_db),
                current_user: schemas.User = Depends(get_current_user)):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=current_user)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} Not found')
    user = blog.filter(models.Blog.user_id == current_user)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='This Post is not yours.')
    blog.delete(synchronize_session=False)
    db.commit()
    return 'Deleted'


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id,
                request: schemas.Blog,
                db: Session = Depends(get_db),
                current_user: schemas.User = Depends(get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} Not found')
    user = blog.filter(models.Blog.id == current_user)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='This Post is not yours.')

    blog.update({'title': request.title, 'body': request.body})
    db.commit()
    return 'Updated'


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show_blog(id,db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {'detail':f'Blog with id {id} Not found'}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with id {id} Not found')

    return blog

