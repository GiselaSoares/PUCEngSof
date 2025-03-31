# meu-app-api/app.py
from fastapi import FastAPI
from .models.livro import LivroModel
from .schemas.livro import LivroCreate, LivroResponse
from .logger import get_logger

# Inicialização da aplicação FastAPI
app = FastAPI()

# Configuração de log
logger = get_logger()

@app.on_event("startup")
async def startup_event():
    logger.info("A aplicação FastAPI foi iniciada.")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("A aplicação FastAPI foi encerrada.")

# Rota para adicionar livro
@app.post("/livros/", response_model=LivroResponse)
async def adicionar_livro(livro: LivroCreate):
    LivroModel.add_livro(livro)
    return livro

# Rota para listar livros
@app.get("/livros/", response_model=list[LivroResponse])
async def listar_livros(status: str = None):
    return LivroModel.get_livros(status)
