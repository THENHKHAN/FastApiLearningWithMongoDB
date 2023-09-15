
from pymongo import MongoClient

mongoUrl = "mongodb+srv://Noorul:<PW>@fastapi-1stapidev.zsfoowr.mongodb.net/"
conn = MongoClient(mongoUrl)

print ("DB connected...........")

