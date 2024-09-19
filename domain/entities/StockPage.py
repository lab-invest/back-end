from typing import List
from pydantic import BaseModel

class StockData(BaseModel):
    nome: str
    rentabilidade: float
    imagem: str
    max: float
    minimo: float
    volume: int
    abertura: float
    fechamento: float
    preco_atual: float

class AdditionalData(BaseModel):
    items: List[StockData] 

class StockPage(BaseModel):
    ibov_points: float
    ibov_rent: float
    additional_data: AdditionalData  
