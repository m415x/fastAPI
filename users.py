from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


# Entidad User
class User(BaseModel):
    name: str
    surname: str
    url: str
    age: int


users_list = [
    User(name="Cristian", surname="Lahoz", url="url", age=37),
    User(name="Cristian", surname="Lahoz", url="url", age=37),
    User(name="Cristian", surname="Lahoz", url="url", age=37),
]


@app.get("/users")
async def users():
    return users_list
