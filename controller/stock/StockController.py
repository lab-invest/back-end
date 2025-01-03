from domain.entities.WalletObject import WalletList, WalletsRequest
from service.stock.StockService import StockService
from typing import Dict, List

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
    
    @classmethod
    def get_image(cls, ticker:str):
        return cls.__service.get_image(ticker)

    @classmethod
    def stockComparison(cls, stockList: List[str]):
        return cls.__service.stockComparison(stockList)
    
    @classmethod
    def stockComparisonAside(cls, stockList: List[dict]):
        return cls.__service.stockComparisonAside(stockList)
    
    @classmethod
    def walletComparison(cls, walletList: WalletsRequest):
        return cls.__service.walletComparison(walletList)
    
    @classmethod
    def walletRent(cls, walletList: List[dict]):
        return cls.__service.getWalletRent(walletList)
    
    @classmethod
    def walletInfo(cls, walletList: WalletsRequest):
        return cls.__service.walletInfo(walletList)
    
    @classmethod
    def findStock(cls, stockName: str):
        return cls.__service.findStock(stockName)