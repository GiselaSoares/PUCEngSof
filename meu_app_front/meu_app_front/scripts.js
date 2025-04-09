// Função para carregar livros lidos da API e exibir na tabela
function carregarLivrosLidos() {
    fetch('/livros_lidos')
        .then(response => response.json())
        .then(livros => {
            const tabelaLivrosLidos = document.getElementById('tabela-livros-lidos').getElementsByTagName('tbody')[0];
            tabelaLivrosLidos.innerHTML = ''; // Limpar a tabela existente
            livros.forEach(livro => {
                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td>${livro.nome}</td>
                    <td>${livro.autor}</td>
                    <td>${livro.genero}</td>
                    <td>${livro.resumo}</td>
                `;
                tabelaLivrosLidos.appendChild(tr);
            });
        });
}

// Função para carregar livros não lidos da API e exibir na tabela
function carregarLivrosNaoLidos() {
    fetch('/livros_nao_lidos')
        .then(response => response.json())
        .then(livros => {
            const tabelaLivrosNaoLidos = document.getElementById('tabela-livros-nao-lidos').getElementsByTagName('tbody')[0];
            tabelaLivrosNaoLidos.innerHTML = ''; // Limpar a tabela existente
            livros.forEach(livro => {
                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td>${livro.nome}</td>
                    <td>${livro.autor}</td>
                    <td>${livro.genero}</td>
                    <td>${livro.resumo}</td>
                `;
                tabelaLivrosNaoLidos.appendChild(tr);
            });
        });
}

// Função para adicionar livro na tabela
function adicionarLivro(event) {
    event.preventDefault();

    // Pegando os valores do formulário
    const nome = document.getElementById('nome').value;
    const autor = document.getElementById('autor').value;
    const genero = document.getElementById('genero').value;
    const resumo = document.getElementById('resumo').value;
    const status = document.getElementById('status').value;

    // Selecionando a tabela de acordo com o status
    const tabela = status === 'lido' ? document.getElementById('tabela-livros-lidos').getElementsByTagName('tbody')[0] : document.getElementById('tabela-livros-nao-lidos').getElementsByTagName('tbody')[0];

    // Criando a linha para o novo livro
    const tr = document.createElement('tr');
    tr.innerHTML = `
        <td>${nome}</td>
        <td>${autor}</td>
        <td>${genero}</td>
        <td>${resumo}</td>
    `;

    // Adicionando a nova linha à tabela
    tabela.appendChild(tr);

    // Limpando os campos do formulário
    document.getElementById('formAdicionarLivro').reset();
}

// Carregar livros ao iniciar a página
window.onload = function() {
    carregarLivrosLidos();
    carregarLivrosNaoLidos();

    // Associando a função ao evento de submit do formulário
    document.getElementById('formAdicionarLivro').addEventListener('submit', adicionarLivro);
};
