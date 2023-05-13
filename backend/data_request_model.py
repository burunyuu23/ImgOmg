from pydantic import BaseModel


class Test(BaseModel):
    id: int
    name: str


class User(BaseModel):
    id: int
    login: str
    password: str
    name: str
    surname: str
    patronymic: str
    email: str
    birthdate: str
    category: int


class Category(BaseModel):
    id: int
    name: str
