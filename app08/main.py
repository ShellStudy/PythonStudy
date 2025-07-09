from fastapi import FastAPI, Form
from typing import Annotated

app = FastAPI()

@app.get("/")
def root():
    return {"data": "안녕하세요."}

@app.get("/test")
def test(a : int):
    return {"A변수": a}

@app.post("/test")
def test(a : Annotated[str, Form()]):
    return {"응답": "OK", "A 변수": a}