from typing import List

from fastapi import FastAPI
from pydantic import BaseModel
import json

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

@app.get("/api01")
def read_root():
    return DB

@app.get("/api02")
def read_json():
    with open("data.json", "r") as f:
        data = json.load(f)
    return data