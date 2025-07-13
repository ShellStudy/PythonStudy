from fastapi import FastAPI
from controller import root, movie

app = FastAPI()
app.include_router(root.ctr)
app.include_router(movie.ctr)