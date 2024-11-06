from pydantic import BaseModel
from typing import List, Dict, Any


class StockComparison(BaseModel):
    stocks: List[Dict[str, Dict]]
    