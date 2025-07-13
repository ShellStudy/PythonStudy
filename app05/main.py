from fastapi import FastAPI
from controller import home
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(home.controller)

origins = [
    "http://localhost",
    "http://localhost:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)