from typing import Dict, List
from pydantic import BaseModel

class StockMarketplace(BaseModel):

    aditional_data: Dict[str, float]
    rentability: float
    historic_values: str
    stock_cotation: float
