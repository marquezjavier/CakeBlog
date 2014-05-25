from cakeashes.mongocon import mongoinit
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId 

class comments():
    creatorId = ""
    image = ""
    body = ""
    email = ""
    name = ""
    inactive = ""
    postId = ""
    ip = ""
    id = ""
    
    def getCommentsForPost(self,postId):
        #Connect to mongo db
        #connection = MongoClient()
        db = mongoinit()
        
        return db.comments.find({"postId" : ObjectId(postId)})
        
    
    def save(self):
        #Connect to mongo db
        #connection = MongoClient()
        db = mongoinit()
        newComment = {}
        
        # Needs a postId
        if self.postId != "":
            newComment["postId"] = ObjectId(self.postId)
            
            if self.id != "":
                newComment['_id'] = ObjectId(self.id)
            
            if self.creatorId != "":
                newComment["creatorId"] = ObjectId(self.creatorId)
            
            if self.email != "":
                newComment["email"] = self.email
                
            if self.body != "":
                newComment["body"] = self.body
                
            if self.name != "":
                newComment["name"] = self.name
                
            if self.image != "":
                newComment["image"] = self.image
                
            if self.inactive != "":
                newComment["inactive"] = self.inactive
                
            if self.ip != "":
                newComment["ip"] = self.ip
            
            return db.comments.save(newComment)