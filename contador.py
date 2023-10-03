from flask import Flask
import mysql.connector

app = Flask(__name__)

# aqui começa o contador de cliques
contador_de_cliques = 0

#  conexão MySQL
db_config = {
    "host": "seu_host_mysql",
    "user": "seu_usuario_mysql",
    "password": "sua_senha_mysql",
    "database": "seu_banco_de_dados",
}

# Funçao que puxa dados do MySQL
def obter_dados_do_mysql(cpf):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    query = "SELECT nome, sobrenome FROM tabela_pessoas WHERE cpf = %s"
    cursor.execute(query, (cpf,))
    
    data = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    return data

@app.route('/')
def home():
    return 'Bem-vindo! Clique <a href="https://dunice.adv.br/">aqui</a> para incrementar o contador.'

@app.route('/clicar')
def clicar():
    global contador_de_cliques
    contador_de_cliques += 1

    # CPF da pessoa
    cpf = "12345678900"  

    # Obter dados da pessoa a partir do MySQL
    pessoa = obter_dados_do_mysql(cpf)

    if pessoa:
        nome, sobrenome = pessoa

        # Calcular o hash baseado no CPF, nome e sobrenome
        hash_data = f"{cpf}{nome}{sobrenome}"
        # usando SHA-256 para calcular o hash
        import hashlib
        hashed_data = hashlib.sha256(hash_data.encode()).hexdigest()

        return f'Contagem de Cliques: {contador_de_cliques}<br>Hash gerado: {hashed_data}'
    else:
        return 'CPF não encontrado na base de dados'

if __name__ == '__main__':
    app.run()
