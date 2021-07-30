from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    # publish limit to 10 blogs
    if published:
        return {'data': f'{limit} published blogs only'}
    else:
        return {'data': f'{limit} blogs only'}


@app.get('/blog/{unpublished}')
def show_unpublished(unpublished):
    return {'data': 'unpublished blogs'}


@app.get('/blog/{id}')
def show_blog(id: int):
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id:int, limit=10):
    return {'data': {'1', '2'}}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def blog(request: Blog):
    return {'data': {'title': request.title, 'body': request.body}}


#
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}
#
#
# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}
