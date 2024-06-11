from pydantic import BaseModel, validator
from domain.enum.KnowledgeType import KnowledgeType

class User(BaseModel):
    cpf: str
    nome: str
    email: str
    senha: str
    experiencia: str
    data_nascimento: str
    saldo: float=10000
    carteiras: object={"geral": {}}
    img_perfil: str="foto de perfil"

    @validator('experiencia')
    def validata_knowledge(cls, value: str) -> str:
        knowledg_values = [enum.value for enum in KnowledgeType]
        if value in knowledg_values:
            return value

        raise TypeError(f"Invalid knowledge type! Received {value}, try one of {knowledg_values}")