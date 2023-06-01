from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['noticias']

@app.route('/')
def index():
    noticias = db.noticias.find()
    return render_template('index.html', noticias=noticias)

@app.route('/adicionar-noticia', methods=['POST'])
def adicionar_noticia():
    titulo = request.form['titulo']
    descricao = request.form['descricao']
    db.noticias.insert_one({'titulo': titulo, 'descricao': descricao})
    return redirect('/')

@app.route('/editar-noticia', methods=['POST'])
def editar_noticia():
    id = request.form['edit-id']
    titulo = request.form['edit-title']
    descricao = request.form['edit-description']
    db.noticias.update_one({'_id': ObjectId(id)}, {'$set': {'titulo': titulo, 'descricao': descricao}})
    return redirect('/')

@app.route('/excluir-noticia', methods=['POST'])
def excluir_noticia():
    id = request.form['delete-id']
    db.noticias.delete_one({'_id': ObjectId(id)})
    return redirect('/')

if __name__ == '__main__':
    app.run()
