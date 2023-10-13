class Clique(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False)
    data_hora = db.Column(db.DateTime, default=datetime.utcnow)
    
    @app.route('/clicar')
def clicar():
    # Obtém a URL clicada a partir dos parâmetros da consulta (query parameters)
    url_clicada = request.args.get('url')

    if url_clicada:
        # Verifica se já existe um registro para a mesma URL
        registro_existente = Clique.query.filter_by(url=url_clicada).first()

        if registro_existente:
            # Se o registro existe, incrementa o número de cliques
            registro_existente.data_hora = datetime.utcnow()
        else:
            # Se o registro não existe, cria um novo registro
            novo_clique = Clique(url=url_clicada)
            db.session.add(novo_clique)

        db.session.commit()

        return 'Clique registrado com sucesso!'
    else:
        return 'URL não fornecida.'

if __name__ == '__main__':
    app.run()
