
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from fastapi.templating import Jinja2Templates
from fastapi import APIRouter
from bson.objectid import ObjectId
from model.model import myNoteModel
from config.mongoConnect import conn 
from schema.noteSchema import noteList ,noteConverterIntoDictOfDB


note = APIRouter()
templates = Jinja2Templates(directory="templates")
# print("con:::::::" , conn)


@note.get("/note")
def showNotes(request:Request):
    data=  noteList(conn.notes.noteUI.find())
    print("my data: " , data)
    context = {
        "request" : request,
        "data":data ,# [{1:2}]
        "test" : [{"a":1}] # for testing

    }
    
    return templates.TemplateResponse('index.html',context)




@note.post("/noteAdd")
async def addNote(request:Request):
      form = await request.form() # for using form () you have to install python-multipart
      formDict = dict(form)
      
      formDict["important"] = True if formDict.get("important") =="on" else False # to check checBOX click or not
      print("formData : " , formDict)
      print("formData note: " , formDict["note"])
      insertNote = conn.notes.noteUI.insert_one(formDict)
      if insertNote.inserted_id:
            return {"message": "Note created successfully", "_id": str(insertNote.inserted_id)}
      else:
            return {"error": "Failed to create note"}




'''
Other way of getmethod to get data from DB without schema:

@note.get("/note",response_class=HTMLResponse)
def showNotes(request: Request):
data_cursor =conn.notes.noteUI.find({})
    print("data: ",data_cursor)
   
    data = []
    for doc in data_cursor:
           data.append(
                  {
                         "id":doc["_id"],
                         "title":doc["title"],
                         "note":doc["note"],
                         "ImpOrNot":doc["important"]
                  }
           )

context = {
        "request" : request,
        "data":data ,# [{1:2}]
        "test" : [{"a":1}] # for testing

    }
    
    return templates.TemplateResponse('index.html',context)

    
POST : to get data from form (UI)

@note.post("/noteAdd")
async def addNote(request:Request):
      form = await request.form() # for using form () you have to install python-multipart
      formDict = dict(form)
      
      formDict["important"] = True if formDict.get("important") =="on" else False # to check checBOX click or not
      print("formData : " , formDict)
      print("formData note: " , formDict["note"])
      insertNote = conn.notes.noteUI.insert_one(formDict)
      if insertNote.inserted_id:
            return {"message": "Note created successfully", "_id": str(insertNote.inserted_id)}
      else:
            return {"error": "Failed to create note"}

'''