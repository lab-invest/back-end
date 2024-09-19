from http.client import HTTPException
from typing import Dict, List
from yahoo_fin.stock_info import get_live_price
from datetime import datetime
from dateutil.relativedelta import relativedelta
import yfinance as yf

from domain.entities.Prevision import PrevisionResponse
from domain.entities.StockMarketplace import StockMarketplace


class StockService:
    
    def cotation(self, ticker:str):
        price = get_live_price(ticker)
        return price
    
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

    def calculate_rentability(self, data):
        first_data = data.head(1)['Close'].iloc[-1]
        last_data = data.tail(1)['Close'].iloc[-1]
        print("fist: ", first_data)
        print("last   ", last_data)
        rentabilidade = ((last_data - first_data) / first_data) * 100
        return rentabilidade
    

    def stock_marketplace(self, ticker: str):
        historical_data_json = self.get_previous_year(ticker)['Close'].reset_index().to_json(orient='records')
        stock_cotation = self.cotation(ticker)
        rentability = self.calculate_rentability(self.get_previous_year(ticker))
        aditional_data = {
            "Open": float(self.get_previous_year(ticker).tail(2)['Open'].iloc[0]),
            "High": float(self.get_previous_year(ticker).tail(2)['High'].iloc[0]),
            "Close": float(self.get_previous_year(ticker).tail(2)['Close'].iloc[0]),
            "Low": float(self.get_previous_year(ticker).tail(2)['Low'].iloc[0]),
            "Volume": float(self.get_previous_year(ticker).tail(2)['Volume'].iloc[0])
        }
        marketplace_data: StockMarketplace = {
            "aditional_data": aditional_data,
            "rentability": rentability,
            "historical_data": historical_data_json,
            "stock_cotation": stock_cotation
        }
        return marketplace_data
    
    def stock_page(self):
        return 'oi'

        


