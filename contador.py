import mysql.connector
from flask import Flask, request

# Configuração da conexão com o banco de dados
conexao = mysql.connector.connect(
    host='localhost',
    port= '3306',
    user='root',
    password='12345678',
    database='cliques'
)

# Crie um cursor
cursor = conexao.cursor()

# Defina a consulta SQL para criar a tabela de cliques
consulta = """
CREATE TABLE cliques (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ip VARCHAR(45),
    data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    contador INT
)
"""

# Verifique se a tabela já existe
check_table_query = "SHOW TABLES LIKE 'Cliques'"
cursor.execute(check_table_query)
result = cursor.fetchone()

if result:
    print("A tabela 'Cliques' já existe.")
else:
    # Execute a consulta SQL para criar a tabela
    cursor.execute(consulta)
    print("A tabela 'Cliques' foi criada com sucesso.")
    
    # Confirme as alterações no banco de dados
conexao.commit()

    # Feche o cursor e a conexão
cursor.close()
conexao.close()

app = Flask(__name__)

# Configuração da conexão com o banco de dados

@app.route('/')
def contador_de_cliques():
    cursor = conexao.cursor()
    
# from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def contador_de_cliques():
    # Este é o local apropriado para acessar request.remote_addr
    ip = request.remote_addr

    return f"IP da máquina da pessoa: {ip}"

if __name__ == '__main__':
    app.run()
    
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

# Fechar o cursor e a conexão quando terminar
cursor.close()
conexao.close()

# Incrementa o contador
novo_contador = contador_atual + 1
print("Novo contador:", novo_contador)

    # Atualiza o contador e registra o IP, data e hora no banco de dados
update_query = "UPDATE Cliques SET contador = %s, ip = %s WHERE id = 1"
cursor.execute(update_query, (novo_contador, ip))
conexao.commit()

cursor.close()

return f"Contagem de cliques: {novo_contador}"

if __name__ == '__main__':
    app.run()