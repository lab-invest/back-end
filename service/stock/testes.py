from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import datetime
import yfinance as yf
from datetime import datetime, timedelta
 

def get_previous_year(ticker: str):
    date = datetime.now() - timedelta(1)
        
    while date.weekday() >= 5: 
        date -= timedelta(1)
    
    date_str = date.strftime("%Y-%m-%d")
    data = yf.download(ticker, start=date_str, interval="1m")
    return data

print(get_previous_year("VALE3.SA"))