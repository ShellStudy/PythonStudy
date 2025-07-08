from fastapi import FastAPI
from controller import root

app = FastAPI()
app.include_router(root.ctr)
