from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"test": 1}

@app.get("/test")
def test(a : int):
    return {"data": 12345 + a}

@app.post("/body")
def body(a : int):
    return {"body": "OK", "data": a}