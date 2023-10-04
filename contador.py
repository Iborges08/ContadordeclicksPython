from flask import Flask, request
import mysql.connector

app = Flask(__name__)

# Configuração de conexão MySQL
db_config = {
    "host": "seu_host_mysql",
    "user": "seu_usuario_mysql",
    "password": "sua_senha_mysql",
    "database": "seu_banco_de_dados",
}

# Função para atualizar o IP no banco de dados
def atualizar_ip_no_banco(ip):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Insere o IP na tabela IPs
    cursor.execute("INSERT INTO ips (ip) VALUES (%s)", (ip,))
    
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

    # Atualizar o IP no banco de dados
    atualizar_ip_no_banco(ip)

    # Atualizar a contagem de cliques no banco de dados
    contador_de_cliques = obter_contagem_de_cliques(cpf)

    return f'Contagem de Cliques: {contador_de_cliques}, Endereço IP: {ip}'

# Rota para registrar o IP
@app.route('/registrar_ip')
def registrar_ip():
    # Obter o endereço IP do cliente
    ip = request.remote_addr

    # Atualizar o IP no banco de dados
    atualizar_ip_no_banco(ip)

    return 'IP registrado com sucesso!'

if __name__ == '__main__':
    app.run()
