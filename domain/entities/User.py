from pydantic import BaseModel, validator
from domain.enum.KnowledgeType import KnowledgeType

class User(BaseModel):
    cpf: int
    nome: str
    email: str
    senha: str
    experiencia: str
    carteiras: object={}

    @validator('experiencia')
    def validata_knowledge(cls, value: str) -> str:
        knowledg_values = [enum.value for enum in KnowledgeType]
        if value in knowledg_values:
            return value

        raise TypeError(f"Invalid knowledge type! Received {value}, try one of {knowledg_values}")