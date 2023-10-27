
from flask import Flask, request, jsonify
import mysql.connector
import hashlib
import datetime

# Configurações do banco de dados
conexao = mysql.connector.connect(
     host='localhost',
     port='3306',
     user='root',
     password='12345678',
     database='dunice'
 )

app = Flask(__name__)

# Configurações do banco de dados


# Função para gerar um hash de 4 números a partir do IP do cliente
def generate_hash(ip):
    hash_obj = hashlib.md5(ip.encode())
    return hash_obj.hexdigest()[:4]

# Rota para capturar o clique no link "https://dunice.adv.br/"
@app.route('/capturar_clique', methods=['GET'])
def capturar_clique_dunice():
    try:
        ip = request.remote_addr
        hash_code = generate_hash(ip)
        data_hora = datetime.datetime.now()

        # Conectar ao banco de dados
        conn = conexao
        cursor = conn.cursor()

        # Inserir os dados na tabela de cliques
        cursor.execute("INSERT INTO cliques(ip, hash_code, data_hora) VALUES (%s, %s, %s)", (ip, hash_code, data_hora))
        conn.commit()

        # conn.close()

        return jsonify({"message": "Clique capturado com sucesso!"})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run()



