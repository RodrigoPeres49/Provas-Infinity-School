from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)


ALUNOS_JSON_PATH = 'alunos.json'

# VERIFICA SE O ARQUIVO JSON EXISTE, SE EXISTIR ELE RETORNA OS DADOS DO ARQUIVO SE NÃO UMA LISTA VAZIA



def obter_alunos():
    if os.path.exists(ALUNOS_JSON_PATH):
        with open(ALUNOS_JSON_PATH, 'r') as file:
            return json.load(file)
    else:
        
        return []
print (obter_alunos())
# ESCREVER DADOS NO ARQUIVO JSON

def salvar_alunos(alunos):
    with open(ALUNOS_JSON_PATH, 'w') as file:
        json.dump(alunos, file, indent=2)

# ROTA PARA PAGINA INICIAL

@app.route('/' ,methods=["GET", "POST"])
def index():
    
    lista_alunos = obter_alunos()
    
    return render_template('index.html', lista_alunos = lista_alunos)

# ROTA PARA A PAGINA DE CADASTRO 

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

# FUNÇÃO PARA CADASTRAR O ALUNO

@app.route('/cadastrar_aluno', methods=['POST'])
def cadastrar_aluno():
    
    # VARIAVEIS NO FORMULARIO
    
    nome = request.form.get('nome')
    idade = request.form.get('idade')
    matricula = request.form.get('matricula')
    
    # OBTER DICIONARIO DAS VARIAVEIS

    if nome == "" or idade == "" or matricula == "":
        return 'Informe todos os campos por favor! <a href="/cadastro">Voltar</a>'
    
    else:
        aluno = {"nome": nome, "idade": idade, "matricula": matricula}
    
        # OBTER OS ALUNOS NO JSON E ADICIONAR OS ALUNOS NO ARQUIVO JSON

        alunos_exist = obter_alunos()

        alunos_exist.append(aluno)

        salvar_alunos(alunos_exist)
    

        return redirect(url_for('cadastro', info='Aluno cadastrado com sucesso!'))



# FUNÇÃO PARA REMOVER O ALUNO PELO NUMERO DA MATRICULA ATRAVES DA ROTA

@app.route('/remover_aluno/<int:matricula>')
def remover_aluno(matricula):
    
    # PEGA OS DADOS DOS ALUNOS NO ARQUIVO
    
    alunos_exist = obter_alunos()
    
    # PERCORRE A LISTA DE ALUNOS PARA ENCONTRAR O ALUNO DA MATRICULA CORRETA
    
    for i in alunos_exist:
        print (i['matricula'])
        # SE ACHOU A MATRICULA ENTAO REMOVE DA LISTA E SALVA A LISTA ATUALIZADA NO ARQUIVO JSON NOVAMENTE
        
        if int(i['matricula']) == matricula:
            alunos_exist.remove(i)
            salvar_alunos(alunos_exist)
            
            return 'Aluno deletado com sucesso <a href="/">Voltar</a>'
    else:
        return 'Aluno não encontrado <a href="/">Voltar</a>'
        


if __name__ == '__main__':
    app.run(debug=True)
