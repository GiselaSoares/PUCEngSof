# API - Minha Biblioteca Pessoal

Esta é a API do projeto Minha Biblioteca Pessoal, construída utilizando o Flask em Python. Ela permite gerenciar a biblioteca pessoal do usuário, com funcionalidades para adicionar livros, listar livros lidos e não lidos e armazenar informações no banco de dados SQLite.

Futuras implementacoes:
> O usuário poderá mover livros da tabela ' Livros não Lidos' para a tabela ' Livros Lidos'
> O usuário poderá incluir livros na tabela 'Lista de Desejos' e mover para a tabela 'Livros não lidos'

# Estrutura do Projeto
A API é composta pelos seguintes arquivos:

**app.py**: Arquivo principal que define as rotas da API, incluindo a funcionalidade para adicionar livros e retornar listas de livros lidos e não lidos.

**schemas/livro.py**: Contém os modelos de dados da API, como a estrutura de um livro.

**create_db.py**: Script que cria o banco de dados SQLite e a tabela necessária para armazenar os livros.

**logger.py**: Configuração do log da API, responsável por registrar as ações e erros durante a execução.

**index.html**: Arquivo HTML para a interface de usuário, se necessário para o frontend da API.

# Funcionalidades
Adicionar Livro: A API permite adicionar um livro à biblioteca, informando título, autor, gênero, resumo e status de leitura.

**Listar Livros Lidos:** A API fornece uma rota para listar todos os livros que foram marcados como "Lidos".

**Listar Livros Não Lidos:** A API fornece uma rota para listar todos os livros que ainda não foram lidos.
