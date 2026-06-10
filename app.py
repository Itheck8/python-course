from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
@app.get('/')
def home():
    return {"message": "Привет мир!"}
@app.get("/users")
def get_users():
    return [
        {"id": 1, "name": "Misha"},
        {"id": 2, "name": "Alex"}
    ]
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"id": user_id, "name": "Misha"}
class User(BaseModel):
    name: str
    age: int

@app.post("/users")
def create_user(user: User):
    return {"message": f"Пользователь {user.name} создан!", "data": user}