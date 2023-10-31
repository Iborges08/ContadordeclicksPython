from flask import Flask, request, jsonify
import mysql.connector
import hashlib
import datetime
from werkzeug.middleware.proxy_fix import ProxyFix  # Importe a extensão ProxyFix

# Configurações do banco de dados
conexao = mysql.connector.connect(
     host='localhost',
     port='3306',
     user='root',
     password='12345678',
     database='dunice'
)

app = Flask(__name__)

# Configurar a extensão ProxyFix para lidar com informações de proxy
app.wsgi_app = ProxyFix(app.wsgi_app)

# Função para gerar um hash de 4 números a partir do IP do cliente
def generate_hash(ip):
    hash_obj = hashlib.md5(ip.encode())
    return hash_obj.hexdigest()[:4]

# Rota para capturar o clique no link "https://dunice.adv.br/"
@app.route('/capturar_clique', methods=['GET'])
def capturar_clique_dunice():
    try:
        ip = request.remote_addr  # Agora, isso capturará o IP real do cliente
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