

from fastapi import FastAPI,Request
from pydantic import BaseModel
from pymongo import MongoClient
from model import Item
# from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId


app = FastAPI()
mongoUrl = "mongodb+srv://Noorul:<password>@fastapi-1stapidev.zsfoowr.mongodb.net/"
conn = MongoClient(mongoUrl)

print ("DB connected...........")

@app.get("/")
def readUser():
    return {"Name": "Created by NHKHAN.."}

@app.get("/items/{item_id}")
def getUserWithId(item_id: int, query: str | None = None):   
    return {"item_id": item_id, "q": q}

@app.get("/data/")
def getDB(): 
    data = conn.notes.notes.find({})  
    print("Data from DB::  ", data)
    print("Data tyep::  ", type(data))
    for i in data :
        print("--> " , i["name"])

    data1 = conn.notes.notes.find_one({})  
    print("Data1 from DB::  ", data1["name"])
    print("Data1 tyep::  ", type(data1))

    pass

@app.get("/res" )
async def getDB(): 
    data = conn.notes.notes.find({})  # return connection object
    lst = []
    for i in data :
        lst.append(
            {
               
                "id":str(i["_id"]),
                "name":i["name"],
                "note":i["note"]
            }
        )

   
    print("lst--> ", lst)
    return {"resp " : lst}



@app.post("/item/note") 
def createNote (note:Item):
    # note = jsonable_encoder(note)
    print(note)
    print(type(note))
    data_to_insert = {
            "_id": note.id,
            "name": note.name,
            "note": note.note
        }

    data = conn.notes.notes.insert_one(data_to_insert)
    if data.inserted_id:
            return {"message": "Note created successfully", "_id": str(data.inserted_id)}
    else:
            return {"error": "Failed to create note"}


@app.put("/item/{item_id}")
def update_note(item_id:int,update_data: dict):
    print(f"id: {item_id}")
    print("Data-body receiving : " , update_data)
    print("note : " , update_data["note"])
    db = conn['notes']  # Replace with your database name
    collection = db['notes']  # Replace with your collection name

    # Use `update_one` to update the document
    result = collection.update_one({"_id": str(item_id)}, {"$set": {"note": update_data["note"]}})

    if result.modified_count == 1:
        return {"message": f"Updated item with ID {item_id}"}
    else:
        return {"message": f"Item with ID {item_id} not found"}

@app.delete("/item/{item_id}")
def delete_note(item_id: int):
    print("id :  " , item_id)
    # Find and delete the item from the in-memory list
    db = conn['notes']  # Replace with your database name
    collection = db['notes']  # Replace with your collection name

    # Use `update_one` to update the document
   
    result = collection.delete_one({"_id": str(item_id)})
    if result.deleted_count == 1:
            return {"message": f"Deleted item with ID {item_id}"}
    else:
            return {"message": f"Item with ID {item_id} not found"}

'''

Certainly! The update_one method in MongoDB allows you to update a single document in a collection that 
matches a specified filter. Let's break down the two arguments you provided:

1) Filter Argument:

{"_id": item_id}: This is the filter or query that specifies which document(s) to update.
In this case, you are filtering documents where the "_id" field matches the value of item_id. 
The _id field is typically a unique identifier for MongoDB documents.

2)Update Argument:

   i) {"$set": {"note": update_data["note"]}}: This is the update operation that you want to perform on 
       the matching document(s).
   ii)  "$set" is a MongoDB update operator that sets the value of a field to a new value. 
       In this case, you are using it to set the value of the "note" field to the new value provided in update_data["note"].


-----------
collection.update_one(filter, new_values, upsert=False, bypass_document_validation=False, collation=None, array_filters=None, session=None)
Parameters: 
 

‘filter’ : A query that matches the document to update.
‘new_values’ : The modifications to apply.
‘upsert’ (optional): If “True”, perform an insert if no documents match the filter.
‘bypass_document_validation’ (optional) : If “True”, allows the write to opt-out of document level validation. Default is “False”.
‘collation’ (optional) : An instance of class: ‘~pymongo.collation.Collation’. This option is only supported on MongoDB 3.4 and above.
‘array_filters’ (optional) : A list of filters specifying which array elements an update should apply. Requires MongoDB 3.6+.
‘session’ (optional) : a class:’~pymongo.client_session.ClientSession’.
'''