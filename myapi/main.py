from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

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

#/hello라는 URL 요청이 발생하면 해당 함수를 실행하여 결과 리턴 : {"message": "안녕하세요~~~~~"}
@app.get("/")
def root():
    return {"message": "여기는 메인화면입니당"}

@app.get("/hello")
def hello():
    return {"message":"안녕하세요~~~~~"}