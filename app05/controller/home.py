from fastapi import APIRouter

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