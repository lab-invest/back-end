from yahoo_fin.stock_info import get_live_price

class StockService:
    
    def cotation(self, ticker:str):
        price = get_live_price(ticker)
        return price
    
    def cotationList(self):
        resultList = [get_live_price("VALE3.SA"), get_live_price("TRPL4.SA"), get_live_price("TAEE3.SA"), get_live_price("NEOE3.SA"), get_live_price("PETR4.SA"), get_live_price("TOTS3.SA"), get_live_price("GOAU4.SA"), get_live_price("KLBN4.SA")]
        return resultList

