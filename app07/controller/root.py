from fastapi import APIRouter

ctr = APIRouter(
    prefix='',
    tags=[],
    responses={404: {"description": "Not found"}}
)

@ctr.get("/")
def root():
    return {"test": 2}