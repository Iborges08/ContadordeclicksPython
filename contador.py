from flask import Flask, request
import mysql.connector

app = Flask(__name__)

#  conexão MySQL
db_config = {
    "host": "seu_host_mysql",
    "user": "seu_usuario_mysql",
    "password": "sua_senha_mysql",
    "database": "seu_banco_de_dados",
}

# Função para atualizar a contagem de cliques no banco de dados
def atualizar_contagem_de_cliques(cpf, ip):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Verifique se já existe uma entrada para o CPF
    cursor.execute("SELECT contador FROM cliques WHERE cpf = %s", (cpf,))
    result = cursor.fetchone()

    if result:
        # Se já existe uma entrada para o CPF, atualize a contagem
        contador = result[0] + 1
        cursor.execute("UPDATE cliques SET contador = %s WHERE cpf = %s", (contador, cpf))
    else:
        # Se não existe uma entrada para o CPF, insira uma nova entrada
        cursor.execute("INSERT INTO cliques (cpf, contador, ip) VALUES (%s, 1, %s)", (cpf, ip))

    conn.commit()
    cursor.close()
    conn.close()

# Função para obter a contagem de cliques do banco de dados
def obter_contagem_de_cliques(cpf):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute("SELECT contador FROM cliques WHERE cpf = %s", (cpf,))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        return result[0]
    else:
        return 0

@app.route('/')
def home():
    # CPF da pessoa
    cpf = "12345678900"

    # Obter o endereço IP do cliente
    ip = request.remote_addr

    # Atualizar a contagem de cliques no banco de dados
    atualizar_contagem_de_cliques(cpf, ip)

    # Obter a contagem de cliques do banco de dados
    contador_de_cliques = obter_contagem_de_cliques(cpf)

    return f'Contagem de Cliques: {contador_de_cliques}, Endereço IP: {ip}'

if __name__ == '__main__':
    app.run()