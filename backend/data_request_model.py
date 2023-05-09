from pydantic import BaseModel


class Test(BaseModel):
    id: int
    name: str


class User(BaseModel):
    id: int
    name: str
    surname: str
    patronymic: str
    email: str
    password: str
    birthdate: str
    category: str
