from infraestructure.mongo.MongoInfra import MongoDBConnector
from domain.entities.Stock import Stock
class MovimentationRepo():
    def __init__(self):
        self.client = MongoDBConnector.get_client()
        self.db = self.client["InvestLab"]
        self.movimentation = self.db["Movimentações"]

    
    def save_order(self, email: str, stock: Stock, operation: str, id_operation: str):
        self.movimentation.insert_one({"id_operacao": id_operation, "usuario": email, "ticker": stock.nome, "quantidade": stock.quantidade, "preco": stock.preco_medio, "tipo_operacao": operation})

