
from typing import List

from pydantic import BaseModel


class WalletItem(BaseModel):
    ticker: str
    quantity: int
    average_price: float

class WalletList(BaseModel):
    name: str
    items: List[WalletItem]

class WalletsRequest(BaseModel):
    wallets: List[WalletList]