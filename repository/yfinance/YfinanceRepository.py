import yfinance as yf
from yahoo_fin.stock_info import get_live_price

class YfinanceRepo:

    @classmethod
    def get_info(cls, ticker: str) -> dict:
        ticker_data: dict = yf.Ticker(ticker).info
        info_subset: dict = {
            'cidade': ticker_data.get('city', None),
            'site': ticker_data.get('website', None),
            'setor': ticker_data.get('industry', None)
        }
        return info_subset
    
    @classmethod
    def get_price(cls, ticker: str) -> float:
        ticker_data: float = get_live_price(ticker)
        return ticker_data

    @classmethod
    def get_historic_price(cls, ticker: str, period: str):
        ticker_data = yf.download(ticker, period)
        return ticker_data




