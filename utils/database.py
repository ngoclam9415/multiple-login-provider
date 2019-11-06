import pymongo
from pymongo import MongoClient
import time
from bson.objectid import ObjectId
from bson.json_util import dumps

class UserDatabase:
    def __init__(self):
        self.cluster = MongoClient("localhost", 27017)
        self.user_db = self.cluster["userdb"]
        self.user_collection = self.user_db["user"]
    
    def insert_user(self, document):
	    self.user_collection.insert_one(document)
	    
    def verify_fb_document(self, document):
        cursors = self.user_collection.find({"$or" : [{"email" : document["email"]}, {"facebook_id" : document["facebook_id"]}]})
        if cursors.count():
            return False
        return True

    def verify_tt_document(self, document):
        cursors = self.user_collection.find({"$or" : [{"email" : document["email"]}, {"twitter_id" : document["twitter_id"]}]})
        if cursors.count():
            return False
        return True

    def verify_default_document(self, document):
        cursors = self.user_collection.find({"email" : document["email"]})
        if cursors.count():
            return False
        return True

if __name__ == "__main__":
    import bcrypt
    database = UserDatabase()
    cursors = database.user_collection.find_one({"email" : "lamnn@athena.studio"})
    password = cursors["password"]
    print(password)
    print(bcrypt.checkpw("123456".encode("utf-8"), password))
