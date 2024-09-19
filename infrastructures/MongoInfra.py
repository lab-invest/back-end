import pymongo
class MongoDBConnector:

    __client = None

    @classmethod
    def get_client(cls):
        if cls.__client is None:
            cls.__client = pymongo.MongoClient(f"mongodb+srv://investlab:investlab123@investlab.gphsjai.mongodb.net/")
        return cls.__client