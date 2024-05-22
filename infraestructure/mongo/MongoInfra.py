import pymongo
# Project
class MongoDBConnector:

    __client = None
    __user = "investlab"
    __password = "investlab123"
    __url = "investlab.gphsjai.mongodb.net"

    @classmethod
    def get_client(cls):
        if cls.__client is None:
            cls.__client = pymongo.MongoClient(f"mongodb+srv://investlab:investlab123@investlab.gphsjai.mongodb.net/")
        return cls.__client