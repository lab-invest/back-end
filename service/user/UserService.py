from domain.entities.User import User
from repository.users.UsersRepository import UserRepo
from controller.exceptions.BadRequestException import BadRequestException
from controller.exceptions.NotFoundException import NotFoundException

class UserService:
    def __init__(self):
        self.__user_repo = UserRepo()

    def register_user(self, user_data):
        try:
            user = User(**user_data.dict())
        except BadRequestException as e:
            raise e("Request Body inválido")
        
        existing_user = self.__user_repo.find_user_by_cpf(user.cpf)
        if existing_user:
            raise BadRequestException("Usuário já cadastrado")        
        self.__user_repo.insert_user(user.dict())
        return "Usuario cadastrado"

    def update_user_field(self, cpf, field_name, new_value):
        valid_fields = ["cpf", "nome", "email", "senha", "experiencia", "carteiras"]
        if field_name not in valid_fields:
            raise BadRequestException("Campo inválido")  
        
        user = self.__user_repo.find_user_by_cpf(cpf)
        if not user:
            raise NotFoundException("Usuario não encontrado")
        self.__user_repo.update_user_field(cpf, field_name, new_value)
        return "Usuario alterado"

    def delete_user(self, cpf):
        user = self.__user_repo.find_user_by_cpf(cpf)
        if not user:
            raise NotFoundException("Usuario não encontrado")
        self.__user_repo.delete_user_by_cpf(cpf)
        return {"success": True}
