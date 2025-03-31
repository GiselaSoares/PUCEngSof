# Minha Biblioteca Pessoal

Este projeto MVP para gerenciamento de biblioteca pessoal. Ele permite adicionar novos livros, classificar livros como "Lidos" ou "Não Lidos" e possui uma funcionalidade para mover livros entre as categorias. O objetivo é fornecer uma interface fácil para gerenciar os livros que usuário já leu e os livros que ainda pretende ler.

## Estrutura do Projeto

O projeto consiste em três arquivos principais:

1. **index.html**: Arquivo HTML que define a estrutura da página, incluindo o cabeçalho, o formulário de cadastro e as tabelas para livros lidos e não lidos.
2. **styles.css**: Arquivo de estilos CSS que define a aparência da página, incluindo as tabelas e os formulários.
3. **scripts.js**: Arquivo JavaScript que adiciona a funcionalidade da aplicação, permitindo mover livros entre as tabelas e adicionar novos livros.

## Funcionalidades

- **Adicionar Livro**: O formulário de cadastro permite adicionar um livro à biblioteca, informando o título, autor, gênero e resumo. O livro pode ser marcado como "Lido" ou "Não lido".
- **Livros Lidos e Não Lidos**: Existe uma tabela para livros "Lidos" e outra para livros "Não lidos". 
    - **Livros Lidos**: Exibe os livros que já foram marcados como lidos.
    - **Livros Não Lidos**: Exibe os livros que ainda não foram lidos. Nessa tabela, você pode mover livros para a categoria "Lidos" clicando em um botão.
- **Lista de Livros Não Lidos**: Livros não lidos podem ser adicionados à lista e movidos para a lista de "Lidos" quando terminados.

## Como Usar

1. **Clonando o repositório**:
   Se você deseja utilizar este projeto em seu próprio computador, siga os seguintes passos:

   ```bash
   git clone https://github.com/seu-usuario/minha-biblioteca-pessoal.git
   cd minha-biblioteca-pessoal
