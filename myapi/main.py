from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.question import question_router

"""
* app 객체 : fastAPI의 핵심 객체. 
* main.py : fastAPI 프로젝트의 전체적인 환경을 설정하는 파일
"""
app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(question_router.router)