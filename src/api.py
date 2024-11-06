import sys
import os

# Adicionando o caminho da pasta 'src'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from routes.api_routes import init_routes  # Ajustado
from server.instancia import server  # Alteração_feita
from flask_restx import Api #importação_bem_secudida

# Cria_a_instância_do_Flask_com_a_função_server()_
app = server()  #  função que cria a instância do Flask

# Cria a instância 
api = Api(app, doc='/swagger') 
# Inicializa as rotas 
init_routes(app,api)

#  Flask
if __name__ == '__main__':
    app.run(debug=True)
