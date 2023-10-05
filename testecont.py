from flask import Flask, request
from datetime import datetime
import hashlib

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bem-vindo! Clique <a href="https://dunice.adv.br/">aqui</a> para acessar nosso site.'

@app.route('/clicar')
def clicar():
    # onde vai puxar o endereço do IP do usuário
    user_ip = request.remote_addr

    #  hash com IP data/hora atual
    hash_info = hashlib.sha256(f"{user_ip}{datetime.utcnow()}".encode()).hexdigest()

    return f'Clique registrado com sucesso!<br>Hash gerado: {hash_info}'

if __name__ == '__main__':
    app.run()
