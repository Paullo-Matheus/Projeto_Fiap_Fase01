import sys
import os

# Adicionando o caminho da pasta 'src'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import Config  # Agora deve funcionar

from flask import Flask
from flasgger import Swagger

# Função que cria a instância do Flask e aplica a configuração
def server():
    app = Flask(__name__)
    Swagger(app)
    app.config.from_object(Config)  # Aplica as configurações da classe Config
    return app