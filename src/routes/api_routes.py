from flask import jsonify, request
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Função para registrar as rotas na instância Flask
def init_routes(app):
    @app.route('/', methods=['GET'])
    def home():
        return "Bem-vindo à aplicação Flask com Requests!"

    @app.route('/get_data', methods=['GET', 'POST'])
    def get_data():
        if request.method == 'GET':
            # URL da API externa para a requisição GET
            url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02'
            response = requests.get(url)
            resposta = response.content

            site = BeautifulSoup(resposta, 'html.parser')
#conseguimos ver os atributos de todas as classes...
            lista=[]
            noticia =site.find('div' , attrs={'class': 'content_center'})
            texto=noticia.find('table',attrs={'class': 'tb_base tb_dados'})
            price=noticia.find('td',attrs={'class': 'tb_subitem'})
            lista.append([texto.text,price.text])
            news=pd.DataFrame(lista,columns=['texto'.strip(),'preço'.strip()])
#para obter somente o texto da tag
            news.to_excel('noticias.xlsx',index=False)

            if response.status_code == 200:
                data = response.json()
                return jsonify(data)
            else:
                return jsonify({"error": "Não foi possível obter os dados"}), 500

        elif request.method == 'POST':
            # Obtenha dados do corpo da requisição
            payload = request.json  # Assume que o corpo da requisição POST está em JSON
            print("Dados recebidos no POST:", payload)
            return jsonify({"message": "Dados recebidos com sucesso!", "data": payload}), 200
