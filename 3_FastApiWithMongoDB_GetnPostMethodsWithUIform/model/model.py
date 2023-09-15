
from pydantic import BaseModel

class myNoteModel(BaseModel):
    title: str
    note: str | None = ""
    important:bool = True

