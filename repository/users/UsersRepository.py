from infraestructure.mongo.MongoInfra import MongoDBConnector
from domain.entities.Stock import Stock
from controller.exceptions.BadRequestException import BadRequestException

class UserRepo():
    def __init__(self):
        self.client = MongoDBConnector.get_client()
        self.db = self.client["InvestLab"]
        self.collection = self.db["Usuarios"]


    def insert_user(self, user_data):
        self.collection.insert_one(user_data)

    def find_user_by_email(self, email: str):
        user = self.collection.find_one({"email": email}, {"_id": 0})
        return user

    def find_user_by_cpf(self, cpf: str):
        user = self.collection.find_one({"cpf": cpf}, {"_id": 0})
        return user

    def update_user_field(self, email: str, field_name: str, new_value: str | float):
        self.collection.update_one({"email": email}, {"$set": {field_name: new_value}})

    def delete_user_by_email(self, email: str):
        self.collection.delete_one({"email": email})

    def update_balance(self, email: str, price: float):
        saldo: float = self.find_user_by_email(email)["saldo"]
        new_price: float = saldo - price
        self.update_user_field(email, "saldo", new_price)
    
    def find_user_balance(self, email: str):
        user_balance = self.collection.find_one({"email": email}, {"saldo": 1, "_id": 0})["saldo"]
        return user_balance
    
    def validate_valid_balance(self, email: str, price: float):
        balance: float = self.find_user_balance(email)
        if price > balance:
            raise BadRequestException("Saldo insuficiente")
    
    def get_average_price(self, email: str, ticker: str):
        user = self.collection.find_one({"email": email})
        return user["carteiras"]["geral"][ticker]
    
    def insert_new_ticker_wallet(self, email, acao: Stock):
        self.collection.update_one(
            {"email": email},
            {"$set": {"carteiras.geral." + acao.nome: {"preco_medio": acao.preco_medio, "quantidade": acao.quantidade}}},
            upsert=True
        )

    def update_exists_ticker_wallet(self, email: str, acao: Stock, preco_medio: float):
        self.collection.update_one(
            {"email": email, "carteiras.geral." + acao.nome: {"$exists": True}},
            {
                "$inc": {"carteiras.geral." + acao.nome + ".quantidade": acao.quantidade},
                "$set": {"carteiras.geral." + acao.nome + ".preco_medio": preco_medio}
            },
            upsert=True
        )

    
    def verify_existing_stock(self, email, ticker):
        return self.collection.count_documents(
            {"email": email, "carteiras.geral." + ticker: {"$exists": True}}
        )
    
    def calculate_new_average_price(self, email: str, stock: Stock) -> float:
        ticker: str = stock.nome
        dado_existente: dict = self.get_average_price(email, ticker)
        quantidade = dado_existente["quantidade"] + stock.quantidade
        valor_atual: float = dado_existente["preco_medio"] * dado_existente["quantidade"]
        nova_compra: float = stock.preco_medio * stock.quantidade
        preco: float = (valor_atual + nova_compra) / quantidade
        return preco
    
