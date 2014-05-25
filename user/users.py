from cakeashes.mongocon import mongoinit
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId 

import md5

class users():
    lastName = ""
    firstName = ""
    email = ""
    userName = ""
    password = ""
    inactive = ""
    admin = ""
    id = ""
    
    def getUser(self, userName):
        # Connect to mongo db
        #connection = MongoClient()
        db = mongoinit()
        
        user = db.users.find_one({"userName" : userName.lower()})
            
        return user
    
    def checkCredentials(self, userName, password):
        # Get the user info
        userInfo = self.getUser(userName.lower())
        
        return userInfo
    
        if userInfo:
            m = md5.new()
            m.update(password)
            if userInfo["password"] == m.hexdigest():
                return userInfo;
               
        return False;

    def userExists(self, userName):
        if self.getUser(userName.lower()):
            return True
        
        return False
    
    def isAdmin(self, userId):
        #connection = MongoClient()
        db = mongoinit()
        
        user = db.users.find_one({"_id" : userId})
        if user["admin"] and user["admin"] == "1":
            return True
        
        return False
    
    def save(self):
        # Connect to mongo db
        #connection = MongoClient()
        db = mongoinit()
        newUser = {}
        
        if self.id != "":
            newUser['_id'] = pymongo.objectid(self.id)
        
        if self.lastName != "":
            newUser["lastName"] = self.lastName
        
        if self.firstName != "":
            newUser["firstName"] = self.firstName
            
        if self.email != "":
            newUser["email"] = self.email
            
        if self.userName != "":
            newUser["userName"] = self.userName.lower()
            
        if self.password != "":
            m = md5.new()
            m.update(self.password)
            newUser["password"] = m.hexdigest()
            
        if self.inactive != "":
            newUser["inactive"] = self.inactive
            
        if self.admin != "":
            newUser["admin"] = self.admin
        
        return db.users.save(newUser)