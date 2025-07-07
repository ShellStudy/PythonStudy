from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    print("App05 Start!!")
    return {"name": "AI"}
