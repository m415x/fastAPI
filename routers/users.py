from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


router = APIRouter(
    prefix="/users", tags=["users"], responses={404: {"message": "No encontrado"}}
)


# Entidad User
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int


users_list = [
    User(id=1, name="Cristian", surname="Lahoz", url="url", age=37),
    User(id=2, name="Cristian", surname="Lahoz", url="url", age=37),
    User(id=3, name="Cristian", surname="Lahoz", url="url", age=37),
    User(id=4, name="Cristian", surname="Lahoz", url="url", age=37),
]


# GET
@router.get("/")
async def users():
    return users_list


# Path
@router.get("/user/{id}")
async def user(id: int):  # type: ignore
    return search_user(id)


# Query
@router.get("/user/")
async def user(id: int):  # type: ignore
    return search_user(id)


# POST
@router.post("/user/", response_model=User, status_code=201)
async def user(user: User):  # type: ignore
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=204, detail="El usuario ya existe")

    users_list.append(user)
    return user


# {"id":5, "name":"Cristian", "surname":"Lahoz", "url":"url", "age":37}


# PUT
@router.put("/user/")
async def user(user: User):  # type: ignore
    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        return {"error": "No se ha actualizado usuario"}

    return user


# DELETE
@router.delete("/user/{id}")
async def user(id: int):
    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True

    if not found:
        return {"error": "No se ha eliminado usuario"}


# Search user
def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)

    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado usuario"}
