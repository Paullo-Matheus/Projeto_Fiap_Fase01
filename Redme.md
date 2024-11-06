# Aplicação no site da Embrapa

> Breve descrição e finalidade do Projeto Embrapa.

![Logo](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSiPWYHFHwW2NR0502jc-w7sC7x6KwduvdTZQ&s) <!-- Se você tiver uma imagem de logo, insira o caminho aqui -->

## Índice

- [Descrição](#descrição)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Pré-Requisitos](#pré-requisitos)
- [Link-Git](#Link-Git)
- [Contato](#contato)
- [Uso](#uso)


## Descrição

Projeto.Aplicação Flask, Objetivo é fazer uma breve requisição no site Embrapa, resolve problemas de quem trabalha no site, assim facilitando a vida do usuário, foi desenvovido no Python/Ide-Vscode.

Exemplo:
- Este é um projeto faz uma aplicação, fazendo uma requisição, e pegando dados em HTML, facilitando o controle de informações.

## Tecnologias Utilizadas

- **Node.js** -  execução do servidor e usar o comando nmp, porém obtive falhas na hora de subir na vercel.
- **Python** - Para o desenvolvimento das API's.
- **Api-Flask** - Framework,para fazer aplicação do site Embrapa.


## Pré-Requisitos

Antes de começar, você precisa ter o seguinte instalado na sua máquina:

- [Node.js](https://nodejs.org/) (Versão 14 ou superior---precisou para usar o comando npm-vercel\porém com falhas)
- [Flask](https://flask.palletsprojects.com/) (Framework)
- [Python](https://python.org.br/instalacao-windows/) (Python)
- [VSCode](https://code.visualstudio.com/download) (IDE)

Se você estiver utilizando o projeto localmente, certifique-se de que o serviço esteja em execução.

## Link-Git

Leia a mensagem com atenção.

1. Clone o repositório:
    ```bash
    git clone https://github.com/Paullo-Matheus/Projeto_Fiap_Fase01.git
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd Projeto_Fiap_Fase01
    ```



 endereço Local `http://localhost:5000/swagger`.


 ## Contato

Paullomatheus.226@gmail.com

RM:259255

## Uso

Segue um exemplo do código api.py em uso.

Exemplo de comando ou código:

```bash


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
Uma breve descrição sobre o que o projeto faz e seu propósito-
.


git clone https://github.com/Paullo-Matheus/Projeto_Fiap_Fase01.git

