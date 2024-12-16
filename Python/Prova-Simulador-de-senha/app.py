from flask import Flask, render_template, render_template_string, request ,url_for, redirect
import os
import json

app = Flask(__name__)

REGISTRO_JSON_PATH = 'senha.json'

# LER O ARQUIVO JSON

def ler_senhas():
    if os.path.exists(REGISTRO_JSON_PATH):
        with open(REGISTRO_JSON_PATH, 'r') as arquivo:
            return json.load(arquivo)
    else:
        return []

# ESCREVER NO ARQUIVO JSON

def escrever_senhas(registro):
    with open(REGISTRO_JSON_PATH, 'w') as arquivo:
        json.dump(registro, arquivo, indent=2)


# ROTAS E FUNÇÕES
        
@app.route('/')
def index():
    info = 'Insira a senha acima.'
    return render_template('index.html', info = info)


# SOMENTE ABRIR A PAGINA DE CADASTRO 

@app.route('/cadastrar')
def pagina_cadastro():
    return render_template('cadastrar_senha.html')

# FUNÇÃO PARA CADASTRAR A SENHA

@app.route('/cadastrar_senha', methods=['POST'])
def cadastrar_senha():
    nome = request.form.get('nome')
    senha = request.form.get('senha')

    # COLOCANDO OS DADOS NO DICIONARIO
    
    registro = [{"nome": nome, "senha": senha}]
    
    # LER DADOS DO JSON
    
    registro_existente = ler_senhas()
    
    # ADICIONAR NOVA SENHA
    
    registro_existente.append(registro)
    
    # ESCREVER NO ARQUIVO JSON
    
    escrever_senhas(registro_existente)
    
    return redirect(url_for('pagina_cadastro'), nome = nome, senha= senha)

if __name__ == '__main__':
    app.run(debug=True)
