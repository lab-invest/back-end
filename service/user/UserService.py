from domain.entities.User import User
from domain.entities.Stock import Stock
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
        return user.dict()
    
    def get_user(self, email: str):
        existing_user = self.__user_repo.find_user_by_email(email)
        if not existing_user:
            raise NotFoundException("Usuário não encontrado")
        return existing_user

    def get_balance(self, email: str):
        existing_user = self.__user_repo.find_user_by_email(email)
        if not existing_user:
            raise NotFoundException("Usuário não encontrado")
        else:
            user_balance = self.__user_repo.find_user_balance(email)
            return user_balance

    def update_user_field(self, email, field_name, new_value) -> None:
        valid_fields = ["cpf", "nome", "email", "senha", "experiencia", "carteiras"]
        if field_name not in valid_fields:
            raise BadRequestException("Campo inválido")  
        
        user = self.__user_repo.find_user_by_email(email)
        if not user:
            raise NotFoundException("Usuario não encontrado")
        self.__user_repo.update_user_field(email, field_name, new_value)

    def delete_user(self, email: str) -> None:
        user = self.__user_repo.find_user_by_email(email)
        if not user:
            raise NotFoundException("Usuario não encontrado")
        self.__user_repo.delete_user_by_email(email)

    def buy_stock(self, email: str, acao: Stock):
        ##TODO: Colocar em Movimentações
        ##TODO: Validar em Ativos
        ##TODO: Tirar do salto
        try:
            stock = Stock(**acao.dict())
        except BadRequestException as e:
            raise e("Request Body inválido")
        
        price = stock.preco_medio * stock.quantidade
        self.__user_repo.validate_valid_balance(email, price)

        verify_existing_stock = self.__user_repo.verify_existing_stock(email, stock.nome)

        if verify_existing_stock > 0:
            new_price = self.__user_repo.calculate_new_average_price(email, stock)
            self.__user_repo.update_exists_ticker_wallet(email, stock, new_price)
        else:
            self.__user_repo.insert_new_ticker_wallet(email, stock)
        
        

        