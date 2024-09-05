from yahoo_fin.stock_info import get_live_price

class StockService:
    # def __init__(self):
    #     self.__user_repo = UserRepo()
    
    def cotation(self, ticker:str):
        price = get_live_price(ticker)
        return price
    
    def cotationList(self, tickers: list):
        resultList = []
        for i in tickers:
            price = get_live_price(i)
            list.append(price)
        return resultList

