from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import app_config
from controller import root, movie

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=app_config.origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(root.ctr)
app.include_router(movie.ctr)
