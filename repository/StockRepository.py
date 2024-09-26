from infrastructures.MongoInfra import MongoDBConnector

class StockRepo():
    def __init__(self):
        self.client = MongoDBConnector.get_client()
        self.db = self.client["InvestLab"]
        self.collection = self.db["Ativos"]

    def get_image(self, ticker):
        return self.collection.find_one({"name": ticker}, {"logo": 1, "_id": 0})
