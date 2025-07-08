from fastapi import Form, APIRouter
from typing import Annotated

ctr = APIRouter()

@ctr.get("/")
def root():
    return {"test": 1}

@ctr.get("/test")
def test(a : int):
    return {"data": 12345 + a}

@ctr.post("/body")
def body(a : Annotated[int, Form(...)]):
    return {"body": "OK", "data": a}