from typing import Dict, List
from pydantic import BaseModel

class StockPage(BaseModel):

    ibov_points: float
    ibov_rent: float
    historic_values: str
    stock_cotation: float
