import pymongo
from pymongo import MongoClient

def mongoinit():
        #connection = MongoClient()
        conn = pymongo.connection.Connection(host="""mongodb://prolatrevol:HuntLan2@127.0.0.1:21192""")
        return conn.cakeAshes
