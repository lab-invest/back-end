from service.user.UserService import UserService
from domain.entities.User import User
from domain.entities.Stock import Stock

class UserController:
    __service = UserService()

    @classmethod
    def register_user(cls, user: User):
        return cls.__service.register_user(user)

    @classmethod
    def update_user_field(cls, email: str, field_name: str, new_value: str):
        return cls.__service.update_user_field(email, field_name, new_value)

    @classmethod
    def delete_user(cls, email: str):
        return cls.__service.delete_user(email)
    
    @classmethod
    def get_user(cls, email: str):
        return cls.__service.get_user(email)

    @classmethod
    def get_balance(cls, email: str):
        return cls.__service.get_balance(email)
    
    @classmethod
    def buy_stock(cls, email: str, stock: Stock, wallet: str):
        return cls.__service.buy_stock(email, stock, wallet)