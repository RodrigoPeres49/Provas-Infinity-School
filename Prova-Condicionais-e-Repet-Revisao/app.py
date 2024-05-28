from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

# CRIANDO O BANCO DE DADOS

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

# DEFIFINDO O APP E A CONFIGURAÇÃO DO BANCO DE DADOS 

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pessoas.db"
db.init_app(app)

# CRIANDO TABELA 

class Pessoa(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    senha: Mapped[str]
    
with app.app_context():
    db.create_all()

# ROTAS E FUNÇÕES

@app.route("/")
def index():
    return render_template('index.html')

# LISTAR PESSOAS

@app.route("/pessoas")
def listar():
    pessoas = db.session.execute(db.select(Pessoa).order_by(Pessoa.nome)).scalars()
    return render_template("lista.html", pessoas=pessoas)

# PAGINA DE CADASTRO

@app.route("/cadastro")
def cadastro():
    return render_template('cadastro.html')

# FUNÇÃO PARA CADASTRAR PESSOA
# CASO O CADASTRO SEJA EFETUADO COM SUCESSO ELE REDIRECIONA PARA A PAGINA DE CADASTRO

@app.route("/cadastrar_pessoa", methods=["GET", "POST"])
def cadastrar_pessoa():
    if request.method == "POST":
        pessoa = Pessoa(
            nome=request.form["nome"],
            email=request.form["email"],
            senha =request.form["senha"]
        )
        db.session.add(pessoa)
        db.session.commit()
        
        return redirect(url_for("cadastro", id = pessoa.id))
        

    return render_template("cadastro.html")

# FUNÇÃO E PAGINA PARA MOSTRAR DADOS DA PESSOA

@app.route("/pessoa/<int:id>/")
def mostrar_pessoa (id):
    pessoa = db.get_or_404(Pessoa, id)
    return render_template("pessoa.html", pessoa=pessoa)

# FUNÇÃO PARA BUSCAR EMAIL DA PESSOA PELO ID

def buscar_id(email):
    id = db.session.query(Pessoa.id).filter_by(email = email).scalar()
    return id

# FUNÇÃO PARA VERIFICAR USUARIO E SENHA 

def verificar_usuario(email, senha):
    
    usuario = Pessoa.query.filter_by(email = email).first()
    
    if usuario and usuario.senha == senha:
        return True
    
    return False

# FUNÇÃO DE LOGIN CASO ELE SEJA EFETUADO COM SUCESSO ELE VAI ATÉ A PÁGINA DOS DADOS DO USUARIO.

@app.route("/verificar_usuario", methods=["GET", "POST"])
def login():
    
    if request.method == "POST":
        
        email = request.form.get('email')
        senha = request.form.get('senha')
        usuario = buscar_id(email)
        print(usuario)
        
        if not email or not senha:
            return 'Insira um usuario e uma senha'
    
        if verificar_usuario(email, senha):
            return redirect(url_for('mostrar_pessoa',id = usuario))
        else:
            return 'Nome de usuário ou senha incorretos' 
    
    return 'Insira um usuario e uma senha'  

# FUNÇÃO PARA APAGAR PESSOA

@app.route("/pessoa/<int:id>/apagar", methods=["GET", "POST"])
def apagar_pessoa(id):
    pessoa = db.get_or_404(Pessoa, id)

    db.session.delete(pessoa)
    db.session.commit()
    return redirect(url_for('listar'))

# FALTOU AS FUNÇÕES DE ALTERAR NOME, SENHA E EMAIL E ALGUMAS MENSAGENS COMO " Cadastro efetuado com sucesso! "

if __name__ == '__main__':
    app.run(debug=True)