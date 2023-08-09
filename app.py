from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Text, Optional
from datetime import datetime
from uuid import uuid4

app = FastAPI()

posts = []

# Post Model
class Post(BaseModel):
    id: Optional[str] = None
    title: str
    author: str
    content: Text
    created_at: datetime = Field(default_factory=datetime.now)
    published_at: Optional[datetime] = None
    published: bool = False

@app.get('/')
def read_root():
    return{'welcome: Welcome to my REST API'}

@app.get('/posts')
def get_posts():
    return posts

@app.post('/posts')
def save_post(post:Post):
    post.id = str(uuid4())
    posts.append(post.model_dump())
    return posts[-1]

@app.get('/posts/{post_id}')
def get_posts(post_id: str):
    for post in posts:
        if post['id'] == post_id:
            return post
    raise HTTPException(status_code=404, detail="Post Not Found")

@app.delete('/posts/{post_id}')
def delete_post(post_id: str):
    for index, post in enumerate(posts):
        if post['id'] == post_id:
            posts.pop(index)
            return {"message": "Post has been deleted succesfully"}
    raise HTTPException(status_code=404, detail="Post Not Found")

@app.put('/posts/{post_id}')
def update_post(post_id: str, updatePost: Post):
    for index, post in enumerate(posts):
        if post['id'] == post_id:
            posts[index]['title'] = updatePost.title
            posts[index]['content'] = updatePost.content
            posts[index]['author'] = updatePost.author
            return {"message": "Post has been updated succesfully"}
    raise HTTPException(status_code=404, detail="Post Not Found")
