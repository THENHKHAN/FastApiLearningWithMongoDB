

from fastapi import FastAPI,Request
from fastapi.staticfiles import StaticFiles
from fastapi import Request
from routers.routes import note 



app = FastAPI()
app.include_router(note)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/testing")
def readUser():
    return {"Name": "This note is Created by NHKHAN.."}


