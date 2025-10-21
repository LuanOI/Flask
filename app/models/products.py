from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    name: str
    preco: float
    descricao: Optional[str] = None
    estoque: int