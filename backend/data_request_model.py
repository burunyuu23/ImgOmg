from pydantic import BaseModel, Field, EmailStr


class Test(BaseModel):
    id: int
    name: str


class User(BaseModel):
    login: str = Field(default=None)
    password: str = Field(default=None)
    name: str = Field(default=None)
    surname: str = Field(default=None)
    patronymic: str = Field(default='')
    email: EmailStr = Field(default=None)
    birthdate: str = Field(default=None)
    category: int = Field(default=None)

    class Config:
        the_schema = {
            "user_demo": {
                "login": "helpmepls",
                "password": "123",
                "name": "Nikolay",
                "surname": "ЮГ",
                "patronymic": "404",
                "email": "help@help.com",
                "birthdate": "2003-05-30",
                "category": "0",
            }
        }


class UserLogin(BaseModel):
    login: str = Field(default=None)
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

    class Config:
        the_schema = {
            "user_demo": {
                'login': 'test_login',
                "email": "help@help.com",
                "password": "123"
            }
        }


class Category(BaseModel):
    name: str

    class Config:
        the_schema = {
            "category_demo": {
                "name": "Админ"
            }
        }


def User_to_UserLogin(user: User):
    return UserLogin(login=user.login, email=user.email, password=user.password)
