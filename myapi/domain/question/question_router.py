from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from domain.question import question_schema
from models import Question

router = APIRouter(
    prefix="/api/question",
)


#question_list 함수의 리턴값이 Question 스키마의 리스트임을 명시``
@router.get("/list", response_model = list[question_schema.Question])
def question_list(db: Session = Depends(get_db)):
    with get_db() as db:
        _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    return _question_list

"""
라우터 파일에는 반드시 APIRouter 인스턴스가 있어야 합니다.
이 라우터 객체를 생성하여 FastAPI에 등록해야 한다.

라우팅 : FastAPI가 요청받은  URL을 해석하여 그에 맞는 함수를 실행하고, 결과를 리턴하는 행위

Depends : 매개변수로 전달받은 함수를 호출하여 그 결과를 리턴
"""