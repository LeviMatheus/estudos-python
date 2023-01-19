from distutils.log import debug
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def raiz():
    return 'Olá mundo'

@app.route('/rota2')
def rota2():
    return '<h1>Esta é a segunda rota da aplicação</h1>'

@app.route('/pessoa/<string:nome>/<string:cidade>')
def pessoa(nome, cidade):
    return jsonify({'nome':nome,'cidade':cidade})

app.run(debug=True)