# meu-app-api/schemas/livro.py
from pydantic import BaseModel

class LivroCreate(BaseModel):
    titulo: str
    autor: str
    genero: str
    resumo: str
    status_leitura: str

class LivroResponse(LivroCreate):
    id: int

    class Config:
        orm_mode = True
