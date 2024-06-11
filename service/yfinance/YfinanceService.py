from repository.yfinance.YfinanceRepository import YfinanceRepo
from controller.exceptions.BadRequestException import BadRequestException

class YfinanceService:
    def __init__(self):
        self.__yfinance_repo = YfinanceRepo()

    @classmethod
    def buy_stock(cls, ticker:str, quantity: int, price: float, balance: float) -> None:
        total_price = price * quantity
        cls.verify_balance(balance, total_price)
        try{
            
        }
    
    @classmethod
    def sell_stock(cls, ticker:str, quantity: int) -> None:
        return
    
    @classmethod
    def verify_balance(cls, balance: float, price: float) -> None:
        if balance < price:
            raise BadRequestException("Saldo insuficiente")
    