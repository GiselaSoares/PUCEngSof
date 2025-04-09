from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Listas para armazenar livros lidos e não lidos
livros_lidos = []
livros_nao_lidos = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/adicionar_livro', methods=['POST'])
def adicionar_livro():
    # Pega os dados do formulário
    nome = request.form['nome']
    autor = request.form['autor']
    genero = request.form['genero']
    resumo = request.form['resumo']
    status = request.form['status']

    # Cria o livro
    livro = {
        'nome': nome,
        'autor': autor,
        'genero': genero,
        'resumo': resumo,
        'status': status
    }

    # Adiciona o livro na lista correspondente
    if status == 'lido':
        livros_lidos.append(livro)
    elif status == 'nao_lido':
        livros_nao_lidos.append(livro)

    return jsonify({"message": "Livro adicionado com sucesso!"})

@app.route('/livros_lidos', methods=['GET'])
def get_livros_lidos():
    return jsonify(livros_lidos)

@app.route('/livros_nao_lidos', methods=['GET'])
def get_livros_nao_lidos():
    return jsonify(livros_nao_lidos)

if __name__ == '__main__':
    app.run(debug=True)
