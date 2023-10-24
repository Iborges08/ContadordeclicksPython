# from flask import Flask, request, jsonify
# import mysql.connector
# import hashlib
# import datetime

# app = Flask(__name__)

# # Configurações do banco de dados
# conexao = mysql.connector.connect(
#     host='localhost',
#     port='3306',
#     user='root',
#     password='12345678',
#     database='dunice'
# )

# # Função para gerar um hash de 4 números a partir do IP do cliente
# def generate_hash(ip):
#     hash_obj = hashlib.md5(ip.encode())
#     return hash_obj.hexdigest()[:4]

# # Rota para registrar um clique via um link
# @app.route('/', methods=['GET'])
# def registrar_clique_via_link():
#     ip = request.remote_addr
#     hash_code = generate_hash(ip)
#     data_hora = datetime.datetime.now()


# # Rota para a raiz do aplicativo
# @app.route('/', methods=['GET'])
# def rota_raiz():
#     return "Olá, mundo!"


    
#     # Conectar ao banco de dados
#     conn = conexao
#     cursor = conn.cursor()
    
#     # Inserir os dados na tabela de cliques
#     cursor.execute("INSERT INTO cliques(ip, hash_code, data_hora, quantidade_de_cliques) VALUES (%s, %s, %s)", (ip, hash_code, data_hora))
#     conn.commit()
    
#     # Obter o ID do clique recém-inserido
#     cursor.execute("SELECT LAST_INSERT_ID()")
#     click_id = cursor.fetchone()[0]
    
#     conn.close()
    
#     return jsonify({"clique_id": click_id})

# if __name__ == '__main__':
#     app.run()




from flask import Flask, request, jsonify
import mysql.connector
import hashlib
import datetime

app = Flask(__name__)

# Configurações do banco de dados
conexao = mysql.connector.connect(
    host='localhost',
    port='3306',
    user='root',
    password='12345678',
    database='dunice'
)

# Função para gerar um hash de 4 números a partir do IP do cliente
def generate_hash(ip):
    hash_obj = hashlib.md5(ip.encode())
    return hash_obj.hexdigest()[:4]

# Rota para a raiz do aplicativo
@app.route('/', methods=['GET'])
def rota_raiz():
    return "Olá, mundo!"

# Rota para registrar um clique via um link
@app.route('/', methods=['GET'])
def registrar_clique_via_link():
    ip = request.remote_addr
    hash_code = generate_hash(ip)
    data_hora = datetime.datetime.now()

    # Conectar ao banco de dados
    conn = conexao
    cursor = conn.cursor()

    # Inserir os dados na tabela de cliques
    cursor.execute("INSERT INTO cliques(ip, hash_code, data_hora, quantidade_de_cliques) VALUES (%s, %s, %s, 1) ON DUPLICATE KEY UPDATE quantidade_de_cliques = quantidade_de_cliques + 1", (ip, hash_code, data_hora))
    conn.commit()

    # Obter o ID do clique recém-inserido
    cursor.execute("SELECT LAST_INSERT_ID()")
    click_id = cursor.fetchone()[0]

    conn.close()

    return jsonify({"clique_id": click_id})

# Rota para capturar o clique em "dunice.adv.br"
@app.route('/DESKTOP-BAQ42COdunice.adv.br/', methods=['GET'])
def capturar_clique_dunice():
    return "Clique capturado."

if __name__ == '__main__':
    app.run()
