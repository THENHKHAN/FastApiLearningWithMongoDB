

from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from config.mongoConnect import conn 

app = FastAPI()
# app.include_router(user)

templates = Jinja2Templates(directory="./templates")
app.mount("/static", StaticFiles(directory="static"), name="static")




@app.get("/testing")
def readUser():
    return {"Name": "This note is Created by NHKHAN.."}



@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request, id: str=None):
    user_name = "John"
    message = "Welcome to FastAPI with Jinja2!"  
    context = {
            "request": request, # mandory if you want to use something in jinja template
            "user_name" :user_name,
            "msg" : message,
            "person":{"name":"Noorul" , "age":25}
    }
    return templates.TemplateResponse("index.html", context)
   
