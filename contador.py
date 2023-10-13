import mysql.connector
from flask import Flask, request

# Conectar-se ao banco de dados
db_connection = mysql.connector.connect(
    host="",
    user="",
    password="",
    database=""
)

app = Flask(__name)

@app.route("/registrar_clique", methods=["GET"])
def registrar_clique():
    # Certifique-se de que a solicitação vem de um gateway confiável, caso seja necessário
    # Por exemplo, você pode verificar o IP do gateway
    ip_gateway = "IP_DO_GATEWAY"  # Substitua pelo IP real do gateway
    if request.remote_addr != ip_gateway:
        return "Acesso não autorizado."

    # Obtenha os parâmetros da solicitação enviada pelo gateway
    ip_address = request.args.get("ip_address")
    nome = request.args.get("nome")
    quantidade_de_click = request.args.get("quantidade_de_click")

    cursor = db_connection.cursor()

    # Inserir um novo clique no banco de dados
    insert_query = "INSERT INTO clicks (ip_address, nome, quantidade_de_click, data_hora) VALUES (%s, %s, %s, NOW())"
    cursor.execute(insert_query, (ip_address, nome, quantidade_de_click))

    db_connection.commit()
    cursor.close()

    return "Clique registrado com sucesso."

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

