from flask import Flask
from view import bp


app = Flask(__name__)


app.register_blueprint(bp)# aqui registra as rotas que estão na view.py ao seu arquivo principal, que é o main.py, para que o Flask saiba onde encontrar as rotas e as funções associadas a elas.

if __name__ == '__main__':
    app.run(debug=True, port=8080)