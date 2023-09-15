

def noteConverterIntoDictOfDB (notes) -> dict: # used to SEND the data from UI or postman to DB
   print("notes : " , notes)
   return   {
                        # "id":str(notes["_id"]),
                        "title":notes["title"],
                        "note":notes["note"],
                        "ImpOrNot":notes["important"]
                }

def noteList (notes) ->list:
     noteList = [noteConverterIntoDictOfDB(note) for note in notes ] # used to get data from DB to dispplay
     return noteList

