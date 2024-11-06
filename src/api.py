import sys
import os

# Adicionando o caminho da pasta 'src'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from routes.api_routes import init_routes  # Ajustado
from server.instancia import server  # Altere conforme necessário

# Cria a instância do Flask com a função server()
app = server()  # Aqui 'server' deve ser a função que cria a instância do Flask

# Inicializa as rotas da aplicação usando a função init_routes()
init_routes(app)

# Inicia o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)
