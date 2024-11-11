from yahoo_fin.stock_info import get_live_price
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from datetime import datetime
import yfinance as yf
from domain.entities.StockComparisonAside import StockComparisonAside
from domain.entities.StockComparison import StockComparison
from domain.entities.WalletObject import WalletList, WalletsRequest
from repository.StockRepository import StockRepo
from domain.entities.Prevision import PrevisionResponse
from domain.entities.StockMarketplace import StockMarketplace
from domain.entities.StockPage import StockPage, StockData, AdditionalData
from typing import Dict, List

##
class StockService:

    def __init__(self):
        self.__user_repo = StockRepo()
        self.stock_page_data = ["VALE3.SA", "TRPL4.SA", "TAEE3.SA", "NEOE3.SA", "PETR4.SA", "TOTS3.SA", "GOAU4.SA", "KLBN3.SA", "BBDC4.SA", "ITUB4.SA", "BBAS3.SA", "CSNA3.SA", "GGBR4.SA", "WEGE3.SA", "RENT3.SA", "RADL3.SA", "ABEV3.SA", "JBSS3.SA"]

    
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
        historical_data_json = self.get_previous_year_by_month(ticker)['Close']
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
        return data.sort_index()

    def get_actual_day(self, ticker: str):
        date = datetime.now().strftime("%Y-%m-%d")
        data = yf.download(ticker, start=date, interval= "1m")
        return data.sort_index()
    
    def get_yesterday(self, ticker: str):
        date = datetime.now() - timedelta(1)
        
        while date.weekday() >= 5: 
            date -= timedelta(1)
        
        date_str = date.strftime("%Y-%m-%d")
        data = yf.download(ticker, start=date_str, interval="1m")
        return data.sort_index()
    
    def get_previous_year_by_month(self, ticker: str):
        date = datetime.now() - timedelta(365)
        
        while date.weekday() >= 5: 
            date -= timedelta(1)
        
        date_str = date.strftime("%Y-%m-%d")
        data = yf.download(ticker, start=date_str, interval="1mo")
        return data.sort_index()
    
    def calculate_rentability(self, data):
        first_data = data.head(1)['Close'].iloc[-1]
        last_data = data.tail(1)['Close'].iloc[-1]
        rentabilidade = ((last_data - first_data) / first_data) * 100
        return rentabilidade
    
    def get_stock_info(self, ticker, info):
        return float(self.get_yesterday(ticker).tail(2)[info].iloc[0])


    def stock_marketplace(self, ticker: str):
        historical_data_json = self.get_previous_year_by_month(ticker)['Close']
        stock_cotation = self.cotation(ticker)
        rentability = self.calculate_rentability(self.get_previous_year(ticker))
        company_name = yf.Ticker(ticker).info.get("longName")
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
            "company_name": company_name,
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
            additional_data_obj.items.append(StockData(nome=i, rentabilidade=self.calculate_rentability(self.get_yesterday(i)), imagem= self.get_image(i), max= self.get_stock_info(i, "High"), minimo= self.get_stock_info(i, "Low"), volume= self.get_stock_info(i, "Volume"), abertura= self.get_stock_info(i, "Open"), fechamento= self.get_stock_info(i, "Close"), preco_atual= self.cotation(i)))
        stock_page = StockPage(
            ibov_points= ibov_points,
            ibov_rent= ibov_rent,
            additional_data = additional_data_obj
        )
        return stock_page
    
    def stockComparison(self, stockList: List[str]):
        result = StockComparison(stocks= [])

        for i in stockList:
            stock = self.get_previous_year_by_month(i)['Close'].to_dict()
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
            stockRent = self.calculate_rentability_by_avg_price(i['average_price'], stockValue)
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
    
    def calculate_rentability_by_avg_price(self, avgPrice: float, price: float):
        return ((price - avgPrice) / avgPrice) * 100
    
    def getWalletRent(self, stockList: List[dict]):
        totalRent = 0
        totalAmountWallet = 0
        for i in stockList:
            stockValue = self.cotation(i['ticker'])
            stockRent = self.calculate_rentability_by_avg_price(i['average_price'], self.cotation(i["ticker"]))
            positionValue = i['quantity'] * stockValue
            totalRent+=stockRent * positionValue
            totalAmountWallet+=positionValue

        if totalAmountWallet == 0 or positionValue == 0: 
            result = 0
        else:
            result = totalRent/totalAmountWallet
        return result
        
    
    def walletComparison(self, wallets_request: WalletsRequest):
        results = []

        for wallet in wallets_request.wallets:
            wallet_value_history = {}
            wallet_name = wallet.name

            for stock in wallet.items:
                ticker = stock.ticker
                quantity = stock.quantity

                historical_data = self.get_previous_year_by_month(ticker)

                for date, row in historical_data.iterrows():
                    close_price = row['Close']
                    position_value = close_price * quantity

                    if date not in wallet_value_history:
                        wallet_value_history[date] = 0
                    
                    wallet_value_history[date] += position_value

            wallet_history_list = [
                {"date": date.strftime("%Y-%m-%d"), "value": value}
                for date, value in sorted(wallet_value_history.items())
            ]

            results.append({
                "wallet_name": wallet_name,
                "history": wallet_history_list
            })

        return results
    
    def walletInfo(self, wallets_request: WalletsRequest):
        wallets_response = {"wallets": []} 

        for wallet in wallets_request.wallets:
            wallet_name = wallet.name
            total_rent = 0
            total_amount_wallet = 0
            items_response = []

            for stock in wallet.items:
                ticker = stock.ticker
                quantity = stock.quantity
                avg_price = stock.average_price
                value = self.cotation(ticker)
                rent = self.calculate_rentability_by_avg_price(avg_price, value)

                stock_value = self.cotation(ticker)
                stock_rent = self.calculate_rentability_by_avg_price(avg_price, stock_value)
                position_value = quantity * stock_value
                total_rent += (stock_rent / 100) * position_value

                total_amount_wallet += position_value

                items_response.append({
                    "ticker": ticker,
                    "value": value,
                    "stock_img": self.get_image(ticker)
                })

            if total_rent == 0 or total_amount_wallet == 0:
                wallet_rent = 0
            else:
                wallet_rent = (total_rent / total_amount_wallet) * 100

            wallets_response["wallets"].append({
                "name": wallet_name,
                "total": total_amount_wallet,
                "rentability": wallet_rent,
                "items": items_response
            })

        return wallets_response

    
    def findStock(self, stockName: str):
        try:
            result = StockData(nome=stockName, rentabilidade=self.calculate_rentability(self.get_yesterday(stockName)), imagem= self.get_image(stockName), max= self.get_stock_info(stockName, "High"), minimo= self.get_stock_info(stockName, "Low"), volume= self.get_stock_info(stockName, "Volume"), abertura= self.get_stock_info(stockName, "Open"), fechamento= self.get_stock_info(stockName, "Close"), preco_atual= self.cotation(stockName))
            return result
        except Exception as e:
            return f"Ação '{stockName}' não encontrada."
