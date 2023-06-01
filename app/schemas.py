from typing import Optional, Generic, TypeVar
from pydantic import BaseModel , Field, EmailStr
from pydantic.generics import GenericModel
from enum import Enum

T = TypeVar('T')


class BookSchema(BaseModel):
    id:Optional[int]
    author: str
    title: str
    description: Optional[str]
    price: int

    class Config:
        orm_mode = True


class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)


class RequestBook(BaseModel):
    parameter: BookSchema = Field(...)


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
    
    
class Roles(Enum):
    user = "user"
    admin = "admin"


class UserSchema(BaseModel):
    email: EmailStr
    username: str
    password: str
    role: Roles = "user"

    class Config:
        orm_mode = True
