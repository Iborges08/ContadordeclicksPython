
# from flask import Flask, request, jsonify
# import mysql.connector
# import hashlib
# import datetime

# conexao = mysql.connector.connect(
#     host='localhost',
#     port='3306',
#     user='root',
#     password='12345678',
#     database='dunice'
# )

# app = Flask(__name__)

# def generate_hash(ip):
#     hash_obj = hashlib.md5(ip.encode())
#     return hash_obj.hexdigest()[:4]

# @app.route('/capturar_clique', methods=['GET'])
# def capturar_clique_dunice():
#     try:
#         ip = request.remote_addr
#         hash_code = generate_hash(ip)
#         data_hora = datetime.datetime.now()

#         conn = conexao
#         cursor = conn.cursor()

#         cursor.execute("INSERT INTO cliques(ip, hash_code, data_hora) VALUES (%s, %s, %s)", (ip, hash_code, data_hora))
#         conn.commit()

#         return jsonify({"message": "Clique capturado com sucesso!"})
#     except Exception as e:
#         return jsonify({"error": str(e)})

# if __name__ == '__main__':
#     app.run()


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
        # Obter o endereço IP local da máquina
        ip = obter_ipv4()
        
        # Se quiser também capturar o endereço IP externo (público), substitua a linha acima por:
        # ip = request.headers.get('X-Forwarded-For', request.remote_addr)

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

