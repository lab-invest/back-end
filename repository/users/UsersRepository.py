from infraestructure.mongo.MongoInfra import MongoDBConnector

class UserRepo():
    def __init__(self):
        self.client = MongoDBConnector.get_client()
        self.db = self.client["InvestLab"]
        self.collection = self.db["Users"]

    def insert_user(self, user_data):
        self.collection.insert_one(user_data)

    def find_user_by_email(self, email):
        user = self.collection.find_one({"email": email})
        return user

    def find_user_by_cpf(self, cpf):
        user = self.collection.find_one({"cpf": cpf}, {"_id": 0})
        return user

    def update_user_field(self, cpf, field_name, new_value):
        self.collection.update_one({"cpf": cpf}, {"$set": {field_name: new_value}})

    def delete_user_by_cpf(self, cpf):
        self.collection.delete_one({"cpf": cpf})