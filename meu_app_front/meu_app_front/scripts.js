// Função para carregar livros lidos da API e exibir na tabela
function carregarLivrosLidos() {
    fetch('/livros_lidos')
        .then(response => response.json())
        .then(livros => {
            const tabela = document.getElementById('tabela-livros-lidos').getElementsByTagName('tbody')[0];
            tabela.innerHTML = ''; // Limpar a tabela existente
            livros.forEach(livro => {
                const tr = criarLinhaLivro(livro);
                tabela.appendChild(tr);
            });
        });
}

// Função para carregar livros não lidos da API e exibir na tabela
function carregarLivrosNaoLidos() {
    fetch('/livros_nao_lidos')
        .then(response => response.json())
        .then(livros => {
            const tabela = document.getElementById('tabela-livros-nao-lidos').getElementsByTagName('tbody')[0];
            tabela.innerHTML = ''; // Limpar a tabela existente
            livros.forEach(livro => {
                const tr = criarLinhaLivro(livro);
                tabela.appendChild(tr);
            });
        });
}

// Função para criar a linha de um livro com botão de remover
function criarLinhaLivro(livro) {
    const tr = document.createElement('tr');
    tr.innerHTML = `
        <td>${livro.nome}</td>
        <td>${livro.autor}</td>
        <td>${livro.genero}</td>
        <td>${livro.resumo}</td>
        <td><button class="remover-livro" title="Remover Livro">❌</button></td>
    `;

    // Evento para remover o livro da tabela
    tr.querySelector('.remover-livro').addEventListener('click', function () {
        tr.remove();
    });

    return tr;
}

// Função para adicionar livro na tabela
function adicionarLivro(event) {
    event.preventDefault();

    const nome = document.getElementById('nome').value;
    const autor = document.getElementById('autor').value;
    const genero = document.getElementById('genero').value;
    const resumo = document.getElementById('resumo').value;
    const status = document.getElementById('status').value;

    const livro = { nome, autor, genero, resumo };

    const tabela = status === 'lido'
        ? document.getElementById('tabela-livros-lidos').getElementsByTagName('tbody')[0]
        : document.getElementById('tabela-livros-nao-lidos').getElementsByTagName('tbody')[0];

    const tr = criarLinhaLivro(livro);
    tabela.appendChild(tr);

    document.getElementById('formAdicionarLivro').reset();
}

// Carregar livros ao iniciar a página
window.onload = function() {
    carregarLivrosLidos();
    carregarLivrosNaoLidos();
    document.getElementById('formAdicionarLivro').addEventListener('submit', adicionarLivro);
};
