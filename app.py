from flask import Flask, jsonify, request, render_template

# criando a aplicação Flask
app = Flask(__name__)

# incluindo a lista de livros
livros = [
    {'id': 1, 'titulo': 'Senhor dos Aneis', 'autor': 'J.R.R Tolkin'},
    {'id': 2, 'titulo': 'Harry Potter', 'autor': 'J.K Howling'}
]

# rota para a página inicial
@app.route('/')
def index():
    return app.send_static_file('index.html')

# rota para obter todos os livros
@app.route('/livro', methods=['GET'])
def obter_livros():
    return jsonify(livros)

# rota para obter um livro pelo id
@app.route('/livro/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
    return jsonify({'erro': 'livro não encontrado'})

# rota para adicionar um livro
@app.route('/livro', methods=['POST'])
def adicionar_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(novo_livro)

# rota para editar um livro pelo id
@app.route('/livro/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
    return jsonify({'erro': 'livro não encontrado'})

# rota para remover um livro pelo id
@app.route('/livro/<int:id>', methods=['DELETE'])
def remover_livro_por_id(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros.pop(indice)
            return jsonify({'mensagem': 'livro removido com sucesso'})
    return jsonify({'erro': 'livro não encontrado'})

# iniciando a aplicação
if __name__ == '__main__':
    app.run(debug=True)