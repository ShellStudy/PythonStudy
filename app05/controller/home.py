from fastapi import APIRouter
from model import users

controller = APIRouter(
    prefix="",
    tags=[],
    responses={404: {"description": "Not found"}}
)

@controller.get("/")
def root():
    print("App05 Start!!")
    return {"name": "AI"}

@controller.get("/data")
def data(d1, d2):
    return {"d1": d1, "d2": d2}

@controller.get("/db")
def db():
    return {"users" : users.findAll()}

@controller.get("/id")
def userId(id):
    return {"user" : users.findOne(id)}