from mongoengine import connect
import os
from dotenv import load_dotenv




def connect_db():
    #fix local prod env setup
    load_dotenv(".env.local")
    print("Connecting to MongoDB...")
    print("Uri: ", os.getenv("MONGO_URI"))
    connect(db='portfolio', host=os.getenv("MONGO_URI"), alias='default')
