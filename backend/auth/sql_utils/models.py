import re
import uuid

from fastapi import HTTPException
from pydantic import BaseModel, EmailStr, validator
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    login = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    patronymic = Column(String, nullable=True)
    email = Column(String, nullable=False, unique=True)
    birthdate = Column(String, nullable=False)
    category = Column(Integer, nullable=False)


FIO_MATCH_PATTERN = re.compile(r"^[а-яёА-ЯЁa-zA-Z\-]+$")


class TunedModel(BaseModel):
    class Config:
        orm_mode = True


class UserProfile(TunedModel):
    user_id: uuid.UUID
    login: str
    email: EmailStr
    name: str
    surname: str
    patronymic: str
    birthdate: str
    category: str


class UserLogin(BaseModel):
    login: str
    email: EmailStr
    password: str


class UserCreate(BaseModel):
    login: str
    password: str
    name: str
    surname: str
    patronymic: str
    email: EmailStr
    birthdate: str
    category: int

