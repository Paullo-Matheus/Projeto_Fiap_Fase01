from flask_restx import Namespace, Resource, fields
from flask import jsonify, request
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Criando um Namespace para a API 
api_namespace = Namespace('data', description='Operações de dados')

# Definindo o modelo de dados para a documentação do Swagger (se necessário para POST)
payload_model = api_namespace.model('Payload', {
    'param1': fields.String(required=True, description='Parâmetro 1'),
    'param2': fields.String(description='Parâmetro 2')
})

# Função para registrar as rotas na instância Flask
def init_routes(app, api):
    api.add_namespace(api_namespace)
    
    @api_namespace.route('/')
    class Home(Resource):
        def get(self):
            """boas-vindas: DE-EMBRAPA"""
            return {"message": "Bem-vindo à aplicação Flask com Requests!"}

    @api_namespace.route('/get_data')
    class GetData(Resource):
        @api_namespace.doc('Obter dados da API externa')
        def get(self):
            """Obtém dados de uma API externa e processa com BeautifulSoup"""
            url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02'
            response = requests.get(url)

            if response.status_code != 200:
                return jsonify({"error": "Não foi possível obter os dados"}), 500

            resposta = response.content
            site = BeautifulSoup(resposta, 'html.parser')

            #  extração -Pag:Produção-EMBRAPA
            lista = []
            noticias = site.find('div', attrs={'class': 'content_center'})

            if noticias:
                for noticia in noticias.find_all('table', attrs={'class': 'tb_base tb_dados'}):
                    texto = noticia.get_text(strip=True)
                    price = noticia.find_next('td', attrs={'class': 'tb_subitem'}).get_text(strip=True)
                    lista.append([texto, price])

                # Convertendo para DataFrame e exportando para Excel
                news = pd.DataFrame(lista, columns=['Texto', 'Preço'])
                news.to_excel('noticias.xlsx', index=False)

                # detalhe não consegui colocar mais páginas pois o site sempre estava fora do ar quando entrei nessa reta final, como tô iniciando, não consigo inspecionar em um site que não funciona, ou só quando bem entender! 

                return jsonify({"message": "Dados extraídos com sucesso!", "data": news.to_dict()}), 200
            else:
                return jsonify({"error": "Dados não encontrados no site"}), 404

        @api_namespace.doc('Recebe dados via POST')
        @api_namespace.expect(payload_model)  # Model para validar o payload
        def post(self):
            """Recebe dados via POST"""
            payload = request.json  #  (assumindo JSON)
            print("Dados recebidos no POST:", payload)
            return jsonify({"message": "Dados recebidos com sucesso!", "data": payload}), 200
