from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Person(BaseModel):
    id: int
    name: str
    age: int 

DB: List[Person] = [
    Person(id=1, name="Camila", age=20),
    Person(id=2, name="Pedro", age=21),
    Person(id=3, name="Van", age=35)
]

@app.get("/api")
def read_root():
    return DB