from pydantic import BaseModel

class Stock(BaseModel):
    nome: str
    preco_medio: float
    quantidade: int 
