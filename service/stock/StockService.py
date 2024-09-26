from yahoo_fin.stock_info import get_live_price
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from datetime import datetime
import yfinance as yf
from repository.StockRepository import StockRepo
from domain.entities.Prevision import PrevisionResponse
from domain.entities.StockMarketplace import StockMarketplace
from domain.entities.StockPage import StockPage, StockData, AdditionalData


class StockService:

    def __init__(self):
        self.__user_repo = StockRepo()
    
    def cotation(self, ticker:str):
        price = get_live_price(ticker)
        return price
    
    def get_image(self, ticker:str):
        return self.__user_repo.get_image(ticker.split(".SA")[0])['logo']
    
    def cotationList(self):
        resultList = [self.cotation("VALE3.SA"), self.cotation("TRPL4.SA"), self.cotation("TAEE3.SA"), self.cotation("NEOE3.SA"), self.cotation("PETR4.SA"), self.cotation("TOTS3.SA"), self.cotation("GOAU4.SA"), self.cotation("KLBN4.SA")]
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
        ibov_points = self.cotation('^BVSP')
        ibov_rent = self.calculate_rentability(self.get_previous_year('^BVSP'))
        stock_page = StockPage(
            ibov_points= ibov_points,
            ibov_rent= ibov_rent,
            additional_data=AdditionalData(
                items=[
                    StockData(nome="VALE3.SA", rentabilidade=self.calculate_rentability(self.get_previous_year('VALE3.SA')), imagem= self.get_image("VALE3.SA"), max= self.get_stock_info("VALE3.SA", "High"), minimo= self.get_stock_info("VALE3.SA", "Low"), volume= self.get_stock_info("VALE3.SA", "Volume"), abertura= self.get_stock_info("VALE3.SA", "Open"), fechamento= self.get_stock_info("VALE3.SA", "Close"), preco_atual= self.cotation("VALE3.SA")),
                    StockData(nome="TRPL4.SA", rentabilidade=self.calculate_rentability(self.get_previous_year('TRPL4.SA')), imagem= self.get_image("TRPL4.SA"), max= self.get_stock_info("TRPL4.SA", "High"), minimo= self.get_stock_info("TRPL4.SA", "Low"), volume= self.get_stock_info("TRPL4.SA", "Volume"), abertura= self.get_stock_info("TRPL4.SA", "Open"), fechamento= self.get_stock_info("TRPL4.SA", "Close"), preco_atual= self.cotation("TRPL4.SA")),
                    StockData(nome="TAEE3.SA", rentabilidade=self.calculate_rentability(self.get_previous_year('TAEE3.SA')), imagem= self.get_image("TAEE3.SA"), max= self.get_stock_info("TAEE3.SA", "High"), minimo= self.get_stock_info("TAEE3.SA", "Low"), volume= self.get_stock_info("TAEE3.SA", "Volume"), abertura= self.get_stock_info("TAEE3.SA", "Open"), fechamento= self.get_stock_info("TAEE3.SA", "Close"), preco_atual= self.cotation("TAEE3.SA")),
                    StockData(nome="NEOE3.SA", rentabilidade=self.calculate_rentability(self.get_previous_year('NEOE3.SA')), imagem= self.get_image("NEOE3.SA"), max= self.get_stock_info("NEOE3.SA", "High"), minimo= self.get_stock_info("NEOE3.SA", "Low"), volume= self.get_stock_info("NEOE3.SA", "Volume"), abertura= self.get_stock_info("NEOE3.SA", "Open"), fechamento= self.get_stock_info("NEOE3.SA", "Close"), preco_atual= self.cotation("NEOE3.SA")),
                    StockData(nome="PETR4.SA", rentabilidade=self.calculate_rentability(self.get_previous_year('PETR4.SA')), imagem= self.get_image("PETR4.SA"), max= self.get_stock_info("PETR4.SA", "High"), minimo= self.get_stock_info("PETR4.SA", "Low"), volume= self.get_stock_info("PETR4.SA", "Volume"), abertura= self.get_stock_info("PETR4.SA", "Open"), fechamento= self.get_stock_info("PETR4.SA", "Close"), preco_atual= self.cotation("PETR4.SA")),
                    StockData(nome="TOTS3.SA", rentabilidade=self.calculate_rentability(self.get_previous_year('TOTS3.SA')), imagem= self.get_image("TOTS3.SA"), max= self.get_stock_info("TOTS3.SA", "High"), minimo= self.get_stock_info("TOTS3.SA", "Low"), volume= self.get_stock_info("TOTS3.SA", "Volume"), abertura= self.get_stock_info("TOTS3.SA", "Open"), fechamento= self.get_stock_info("TOTS3.SA", "Close"), preco_atual= self.cotation("TOTS3.SA")),
                    StockData(nome="GOAU4.SA", rentabilidade=self.calculate_rentability(self.get_previous_year('GOAU4.SA')), imagem= self.get_image("GOAU4.SA"), max= self.get_stock_info("GOAU4.SA", "High"), minimo= self.get_stock_info("GOAU4.SA", "Low"), volume= self.get_stock_info("GOAU4.SA", "Volume"), abertura= self.get_stock_info("GOAU4.SA", "Open"), fechamento= self.get_stock_info("GOAU4.SA", "Close"), preco_atual= self.cotation("GOAU4.SA")),
                    StockData(nome="KLBN3.SA", rentabilidade=self.calculate_rentability(self.get_previous_year('KLBN3.SA')), imagem= self.get_image("KLBN3.SA"), max= self.get_stock_info("KLBN3.SA", "High"), minimo= self.get_stock_info("KLBN3.SA", "Low"), volume= self.get_stock_info("KLBN3.SA", "Volume"), abertura= self.get_stock_info("KLBN3.SA", "Open"), fechamento= self.get_stock_info("KLBN3.SA", "Close"), preco_atual= self.cotation("KLBN3.SA")),
                ]
            )
        )
        return stock_page

        