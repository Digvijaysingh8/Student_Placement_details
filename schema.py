from pydantic import BaseModel


class Student(BaseModel):
    roll: int
    name: str
    marks: float
    address: str
    placed: bool