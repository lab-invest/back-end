from service.user.UserService import UserService
from domain.entities.User import User

class UserController:
    __service = UserService()

    @classmethod
    def register_user(cls, user: User):
        return cls.__service.register_user(user)

    @classmethod
    def update_user_field(cls, cpf: str, field_name: str, new_value: str):
        return cls.__service.update_user_field(cpf, field_name, new_value)

    @classmethod
    def delete_user(cls, cpf: str):
        return cls.__service.delete_user(cpf)
    
    @classmethod
    def get_user(cls, cpf: str):
        return cls.__service.get_user(cpf)