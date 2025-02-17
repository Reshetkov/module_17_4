from pydantic import BaseModel


class CreateUser(BaseModel):
    username: str
    firstname: str
    age: int
    slug: str
    lastname: str
    id: int


class UpdateUser(BaseModel):
    firstname: str
    lastname: str
    age: int


class CreateTask(BaseModel):
    title: str
    content: str
    priority: int


class UpdateTask(BaseModel):
    title: str
    content: str
    priority: int