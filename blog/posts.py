from cakeashes.mongocon import mongoinit
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId 

class posts():
    creatorId = ""
    categoryId = ""
    image = ""
    title = ""
    body = ""
    tags = {}
    inactive = ""
    ip = ""
    id = ""
    
    def getLatestBlogs(self):
        #Connect to mongo db
        #connection = MongoClient()
        db = mongoinit()
        
        postList = []
        for post in db.posts.find().sort("_id", -1):
            post['id'] = post["_id"]
            post['dateCreated'] = post["_id"].generation_time
            
            tagList = []
            tagList = db.tags.find({"postsTagged" : post["_id"] },{"name" : 1, "_id" : 1})
                
            post['tags'] = tagList
            
            post['author'] = db.users.find_one({"_id" : post['creatorId']})
            
            post['commentCount'] = db.comments.find({"postId" : ObjectId(post["_id"])}).count()
            
            postList.append(post)
            
        return postList
    
    def getPost(self,postId):
        #Connect to mongo db
        #connection = MongoClient()
        db = mongoinit()
        
        post  = db.posts.find_one({"_id" : ObjectId(postId)})
        post['id'] = post["_id"]
        post['dateCreated'] = post["_id"].generation_time;
        
        tagList = db.tags.find({"postsTagged" : post["_id"] },{"name" : 1, "_id" : 1})
            
        post['tags'] = tagList
        
        post['author'] = db.users.find_one({"_id" : post['creatorId']})
            
            
        return post
    
    def deletePost(self,postId):
        #Connect to mongo db
        #connection = MongoClient()
        db = mongoinit()
        
        db.posts.remove({"_id" : ObjectId(postId)})
    
    
    def save(self):
        #Connect to mongo db
        #connection = MongoClient()
        db = mongoinit()
        newPost = {}
        
        if self.id != "":
            newPost['_id'] = ObjectId(self.id)
        
        if self.creatorId != "":
            newPost["creatorId"] = ObjectId(self.creatorId)
        
        if self.categoryId != "":
            newPost["categoryId"] = self.categoryId
            
        if self.title != "":
            newPost["title"] = self.title
            
        if self.body != "":
            newPost["body"] = self.body
            
        if self.image != "":
            newPost["image"] = self.image
            
        if self.inactive != "":
            newPost["inactive"] = self.inactive
            
        if self.ip != "":
            newPost["ip"] = self.ip
            
        postId = db.posts.save(newPost)
        
        if self.tags != {}:
            for tag in self.tags:
                if tag != "":
                    tagName = tag.strip()
                    db.tags.update({"name" : tagName},{"$push" : {"postsTagged" : postId}},True,False)
        
        return postId
        