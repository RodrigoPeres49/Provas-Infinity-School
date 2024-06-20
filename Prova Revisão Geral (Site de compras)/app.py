from flask import Flask
from db import db
from models import *
from atenticacao import login_manager
from controllers.controles_produto import produto_bp
from controllers.controles_usuario import cliente_bp

# FIZ SOMENTE AS OPERAÇÕES BACK END AS DEMAIS FUNÇÕES ESTÃO EM DESENVOLVIMENTO

# PARA TESTAR O APLICATIVO COLOQUEI DOIS USUARIOS PARA TESTE

# 1- Usuario: COMPRADOR1, senha: 123456
# 2- Usuario: COMPRADOR2, senha:159159

# INCIANDO APP FLASK

app = Flask(__name__)

# BANDO DE DADOS NO ARQUIVO clientes.db

app.config["SECRET_KEY"] = ' '
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///clientes.db"

# BLUE PRINT DOS CLIENTES E DOS PRODUTOS A VENDA na pasta controllers

app.register_blueprint(produto_bp)
app.register_blueprint(cliente_bp)

# INICIANDO BANCO DE DADOS E CRIANDO O ARQUIVO clientes.db SE NÃO EXISTIR

db.init_app(app)

with app.app_context():
    
    # LOGIN MANAGER INICIANDO
    
    login_manager.init_app(app)
    db.create_all()

# EXECUTANDO ARQUIVO

if __name__ == '__main__':
    app.run(debug=True)