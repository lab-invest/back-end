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



print(yf.Ticker("SANB11.SA").info.get("longName"))