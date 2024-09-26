from typing import Dict, List
from pydantic import BaseModel

class PrevisionResponse(BaseModel):

    previsioned_value: float
    rentability: float
    historic_values: str
