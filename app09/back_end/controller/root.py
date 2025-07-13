from fastapi import APIRouter

ctr = APIRouter(tags=["root"])

@ctr.get("/")
def root():
    return {"status": True}