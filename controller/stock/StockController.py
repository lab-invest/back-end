from service.stock.StockService import StockService

class StockController:
    __service = StockService()

    @classmethod
    def get_cotation(cls, ticker: str):
        return cls.__service.cotation(ticker)

    
    @classmethod
    def get_cotation_list(cls):
        return cls.__service.cotationList()
    
    @classmethod
    def get_stock_prevision(cls, ticker: str):
        return cls.__service.stock_prevision(ticker)
    
    @classmethod
    def get_stock_marketplace(cls, ticker: str):
        return cls.__service.stock_marketplace(ticker)
    
    @classmethod
    def get_stock_page(cls):
        return cls.__service.stock_page()
