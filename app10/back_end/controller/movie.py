from fastapi import APIRouter, Form
from typing import Annotated
from config import app_config
import httpx

ctr = APIRouter(prefix="/movie", tags=["movie"])
base_url = f"https://www.omdbapi.com/?apikey={app_config.api_key}"

@ctr.post("/")
async def movie(q : Annotated[str, Form(...)]):
    if q == '' : return {"Response" : False}
    async with httpx.AsyncClient() as client:
        url = f"{base_url}&s={q}"
        response = await client.get(url)
        return response.json()
    
@ctr.post("/findOne")
async def findOne(id : Annotated[str, Form(...)]):
    async with httpx.AsyncClient() as client:
        url = f"{base_url}&i={id}&plot=full"
        response = await client.get(url)
        result = response.json()
        print(result)
        
        # 문제 검색한 영화 내용을 'movie_logs' 테이블에 데이터를 입력하기 (아래 SQL를 이용하세요.)
        # sql = f"INSERT INTO movie_logs (imdbID, title, poster) VALUE ('{imdbID}', '{title}', '{poster}')"
        
        return result