from pydantic import BaseModel
import datetime
class Question(BaseModel):
    id:int
    subject:str | None = None
    content:str
    create_date:datetime.datetime