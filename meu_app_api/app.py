import sys
import os

# Adiciona o diretório raiz ao sys.path para encontrar meu_app_api
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, request, jsonify, render_template
from flask_restx import Api, Resource, fields
from model.livro import LivroModel
import logging

app = Flask(__name__)
api = Api(app, version='1.0', title='API de Livros', description='Uma API simples para gerenciar livros lidos e não lidos')

# Definir o namespace (agrupamento de endpoints)
livros_ns = api.namespace('livros', description='Operações relacionadas a livros')

# Definindo o modelo de dados que será usado para validar as entradas
livro_model = api.model('Livro', {
    'titulo': fields.String(required=True, description='Título do livro'),
    'autor': fields.String(required=True, description='Autor do livro'),
    'genero': fields.String(required=True, description='Gênero do livro'),
    'resumo': fields.String(required=True, description='Resumo do livro'),
    'status_leitura': fields.String(required=True, description='Status do livro (lido/não lido)')
})

# Lista para armazenar livros lidos e não lidos
livros_lidos = []
livros_nao_lidos = []

@app.route('/')
def index():
    return render_template('index.html')

@livros_ns.route('/adicionar_livro')
class AdicionarLivro(Resource):
    @api.expect(livro_model)
    def post(self):
        # Pega os dados do formulário
        data = request.get_json()
        nome = data['titulo']
        autor = data['autor']
        genero = data['genero']
        resumo = data['resumo']
        status = data['status_leitura']

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

@livros_ns.route('/livros_lidos')
class LivrosLidos(Resource):
    def get(self):
        return jsonify(livros_lidos)

@livros_ns.route('/livros_nao_lidos')
class LivrosNaoLidos(Resource):
    def get(self):
        return jsonify(livros_nao_lidos)

if __name__ == '__main__':
    app.run(debug=True)
