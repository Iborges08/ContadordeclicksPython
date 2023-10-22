import mysql.connector
from flask import Flask, request

# Configuração da conexão com o banco de dados
conexao = mysql.connector.connect(
    host='localhost',
    port='3306',
    user='root',
    password='12345678',
    database='cliques'
)

# Criar um objeto cursor
cursor = conexao.cursor()

# Consulta para recuperar o contador atual
consulta = "SELECT contador FROM Cliques WHERE id = 1"
cursor.execute(consulta)
resultado = cursor.fetchone()

if resultado is not None:
    contador_atual = resultado[0]
else:
    contador_atual = 0

# Incrementa o contador
novo_contador = contador_atual + 1

# Atualiza o contador e registra o IP, data e hora no banco de dados
update_query = "UPDATE Cliques SET contador = %s, ip = %s WHERE id = 1"
cursor.execute(update_query, (novo_contador, request.remote_addr))
conexao.commit()

# Fechar o cursor e a conexão
cursor.close()
conexao.close()

app = Flask(__name__)

@app.route('/')
def contador_de_cliques():
    return f"Contagem de cliques: {novo_contador}"

if __name__ == '__main__':
    app.run()
