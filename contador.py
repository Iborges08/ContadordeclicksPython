from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import hashlib

app = Flask(__name__)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://seu_usuario:sua_senha@localhost/sua_base_de_dados'
db = SQLAlchemy(app)

# Modelo da tabela para armazenar os cliques
class Clique(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hash_info = db.Column(db.String(64), nullable=False, unique=True)
    data_hora = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
def home():
    return 'Bem-vindo! Clique <a href="https://dunice.adv.br/">aqui</a> para acessar nosso site.'

@app.route('/clicar')
def clicar():
    # onde vai puxar o endereço do ip do usuario 
    user_ip = request.remote_addr

    # Criar um hash com base no IP e na data/hora atual
    hash_info = hashlib.sha256(f"{user_ip}{datetime.utcnow()}".encode()).hexdigest()

    # Salvar o clique na base de dados com o hash gerado
    novo_clique = Clique(hash_info=hash_info)
    db.session.add(novo_clique)
    db.session.commit()

    return 'Clique registrado com sucesso!'

if __name__ == '__main__':
    app.run()
