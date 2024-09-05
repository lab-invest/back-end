from service.stock.StockService import StockService

class StockController:
    __service = StockService()

    @classmethod
    def get_cotation(cls, ticker: str):
        return cls.__service.cotation(ticker)

    
    @classmethod
    def get_cotation_list(cls):
        return cls.__service.cotationList()
