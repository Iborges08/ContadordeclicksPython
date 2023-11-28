
from flask import Flask, request, jsonify
import mysql.connector
import hashlib
import datetime
import socket

conexao = mysql.connector.connect(
    host='localhost',
    port='3306',
    user='root',
    password='12345678',
    database='dunice'
)

app = Flask(__name__)

def generate_hash(ip):
    hash_obj = hashlib.md5(ip.encode())
    return hash_obj.hexdigest()[:4]

def obter_ipv4():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    return ip_address

@app.route('/capturar_clique', methods=['GET'])
def capturar_clique_dunice():
    try:
       
        ip = obter_ipv4()
        
        hash_code = generate_hash(ip)
        data_hora = datetime.datetime.now()

        conn = conexao
        cursor = conn.cursor()

        cursor.execute("INSERT INTO cliques(ip, hash_code, data_hora) VALUES (%s, %s, %s)", (ip, hash_code, data_hora))
        conn.commit()

        return jsonify({"message": "Clique capturado com sucesso!"})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run()

