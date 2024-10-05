from yahoo_fin.stock_info import get_live_price
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from datetime import datetime
import yfinance as yf
from domain.entities.StockComparisonAside import StockComparisonAside
from domain.entities.StockComparison import StockComparison
from repository.StockRepository import StockRepo
from domain.entities.Prevision import PrevisionResponse
from domain.entities.StockMarketplace import StockMarketplace
from domain.entities.StockPage import StockPage, StockData, AdditionalData
from typing import List


class StockService:

    def __init__(self):
        self.__user_repo = StockRepo()
        self.stock_page_data = ["VALE3.SA", "TRPL4.SA", "TAEE3.SA", "NEOE3.SA", "PETR4.SA", "TOTS3.SA", "GOAU4.SA", "KLBN3.SA"]
    
    def cotation(self, ticker:str):
        price = get_live_price(ticker)
        return price
    
    def get_image(self, ticker:str):
        return self.__user_repo.get_image(ticker.split(".SA")[0])['logo']
    
    def cotationList(self):
        resultList = [self.calculate_rentability(self.get_yesterday('VALE3.SA')), self.calculate_rentability(self.get_yesterday("TRPL4.SA")), self.calculate_rentability(self.get_yesterday("TAEE3.SA")), self.calculate_rentability(self.get_yesterday("NEOE3.SA")), self.calculate_rentability(self.get_yesterday("PETR4.SA")), self.calculate_rentability(self.get_yesterday("TOTS3.SA")), self.calculate_rentability(self.get_yesterday("GOAU4.SA")), self.calculate_rentability(self.get_yesterday("KLBN4.SA"))]
        return resultList
    
    def stock_prevision(self, ticker:str):
        previsioned_value = self.get_prevision(self.get_previous_year(ticker))
        historical_data_json = self.get_previous_year(ticker)['Close'].reset_index().to_json(orient='records')
        rentability = self.calculate_rentability(self.get_previous_year(ticker))
        prevision: PrevisionResponse = {
            "previsioned_value": previsioned_value,
            "rentability": rentability,
            "historical_data": historical_data_json
        }
        return prevision


    def get_prevision(self, data):      
        valor_investido = 1000       
        valor_final = valor_investido * (1 + self.calculate_rentability(data) / 100)
        return valor_final
    
    def get_previous_year(self, ticker: str):
        date = (datetime.now() - relativedelta(years=1)).strftime("%Y-%m-%d")
        data = yf.download(ticker, start=date)
        return data

    def get_actual_day(self, ticker: str):
        date = datetime.now().strftime("%Y-%m-%d")
        data = yf.download(ticker, start=date, interval= "1m")
        return data
    
    def get_yesterday(self, ticker: str):
        date = (datetime.now() - timedelta(1)).strftime("%Y-%m-%d")
        data = yf.download(ticker, start=date, interval= "1m")
        return data

    def calculate_rentability(self, data):
        first_data = data.head(1)['Close'].iloc[-1]
        last_data = data.tail(1)['Close'].iloc[-1]
        rentabilidade = ((last_data - first_data) / first_data) * 100
        return rentabilidade
    
    def get_stock_info(self, ticker, info):
        return float(self.get_yesterday(ticker).tail(2)[info].iloc[0])


    def stock_marketplace(self, ticker: str):
        historical_data_json = self.get_yesterday(ticker)['Close']
        stock_cotation = self.cotation(ticker)
        rentability = self.calculate_rentability(self.get_previous_year(ticker))
        img = self.get_image(ticker)
        aditional_data = {
            "Open": self.get_stock_info(ticker, "Open"),
            "High": self.get_stock_info(ticker, "High"),
            "Close": self.get_stock_info(ticker, "Close"),
            "Low": self.get_stock_info(ticker, "Low"),
            "Volume": self.get_stock_info(ticker, "Volume")
        }
        marketplace_data: StockMarketplace = {
            "aditional_data": aditional_data,
            "rentability": rentability,
            "historical_data": historical_data_json,
            "stock_cotation": stock_cotation,
            "img": img
        }
        return marketplace_data
    
    def stock_page(self):
        additional_data_obj = AdditionalData(items=[])
        ibov_points = self.cotation('^BVSP')
        ibov_rent = self.calculate_rentability(self.get_previous_year('^BVSP'))
        for i in self.stock_page_data:
            additional_data_obj.items.append(StockData(nome=i, rentabilidade=self.calculate_rentability(self.get_previous_year(i)), imagem= self.get_image(i), max= self.get_stock_info(i, "High"), minimo= self.get_stock_info(i, "Low"), volume= self.get_stock_info(i, "Volume"), abertura= self.get_stock_info(i, "Open"), fechamento= self.get_stock_info(i, "Close"), preco_atual= self.cotation(i)))
        stock_page = StockPage(
            ibov_points= ibov_points,
            ibov_rent= ibov_rent,
            additional_data = additional_data_obj
        )
        return stock_page
    
    def stockComparison(self, stockList: List[str]):
        result = StockComparison(stocks= [])

        for i in stockList:
            stock = self.get_previous_year(i)['Close'].to_dict()
            result.stocks.append({i: stock})
        return result
    
    def stockComparisonAside(self, stockList: List[dict]):
        result = StockComparisonAside(stocks=[], walletRent=0.0, totalWallet=0.0)
        result.stocks.append(self.getStockInfoForAside(stockList))
        result.walletRent = self.getWalletRent(stockList)
        result.totalWallet = self.getTotalWalletAmount(stockList)
        return result

    def getStockInfoForAside(self, stockList: List[dict]):
        result = []
        for i in stockList:
            stockValue = self.cotation(i['ticker'])
            stockRent = self.calculate_rentability(self.get_previous_year(i['ticker']))
            stockImg = self.get_image(i['ticker'])
            result.append({i['ticker']: [stockValue, stockRent, stockImg]})
        return result
    
    def getTotalWalletAmount(self, stockList: List[dict]):
        totalAmountWallet = 0
        for i in stockList:
            stockValue = self.cotation(i['ticker'])
            positionValue = i['quantity'] * stockValue
            totalAmountWallet+=positionValue
        return totalAmountWallet
    
    def getWalletRent(self, stockList: List[dict]):
        totalRent = 0
        totalAmountWallet = 0
        for i in stockList:
            stockValue = self.cotation(i['ticker'])
            stockRent = self.calculate_rentability(self.get_previous_year(i['ticker']))
            positionValue = i['quantity'] * stockValue
            totalRent+=stockRent * positionValue
            totalAmountWallet+=positionValue
        result = totalRent/totalAmountWallet
        return result
        