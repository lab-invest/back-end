from pydantic import BaseModel
from typing import List, Dict, Any


class StockComparisonAside(BaseModel):
    stocks: List[Dict[str, List]]
    walletRent: float
    totalWallet: float
    