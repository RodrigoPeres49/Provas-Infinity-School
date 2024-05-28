from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy, session
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column ,DeclarativeBase, relationship

# CRIANDO APLICATIVO E BANCO DE DADOS

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///alunos.db"

db.__init__(app)

# CRIANDO TABELA ALUNOS

class Alunos(db.Model):
    
    __tablename__ = "alunos_tabela"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(nullable=False)
    idade: Mapped[int] = mapped_column(nullable=False)
    turma: Mapped[str] = mapped_column(nullable=False)
    telefone: Mapped[str] = mapped_column(unique=True, nullable=False)
    
    portugues: Mapped[int]
    matematica: Mapped[int]
    geografia: Mapped[int]
    ciencias: Mapped[int]
    ingles: Mapped[int]

    
# CRIAR TABELAS

with app.app_context():
    db.create_all()

# ROTA PRINCIPAL

@app.route('/')
def index():
    return render_template('index.html')

# PAGINA DE CADASTRO 

@app.route('/cadastrar')
def pagina_cadastro():
    return render_template('alunos/cadastrar.html')

# FUNÇÃO PARA CADASTRAR O ALUNO, SE O CADASTRO FOR EFETUADO COM SUCESSO, RETORNA A PAGINA DE CADASTRO

@app.route('/cadastrar_aluno', methods=["GET", "POST"])
def cadastrar_aluno():
    if request.method == "POST":
        aluno = Alunos(
            nome = request.form["nome"],
            idade = request.form["idade"],
            turma = request.form["turma"],
            telefone = request.form["telefone"],
            portugues = 0,
            matematica = 0,
            geografia = 0,
            ciencias = 0,
            ingles = 0,
        )
        
        db.session.add(aluno)
        db.session.commit()
        return redirect(url_for('pagina_cadastro'))
    
    return render_template('alunos/cadastrar.html')

# LISTAR OS ALUNOS

@app.route('/listar_alunos')
def listar_alunos():
    alunos = db.session.execute(db.select(Alunos).order_by(Alunos.nome)).scalars()
    return render_template('alunos/lista_alunos.html', alunos = alunos)

# VISUALIZAR ALUNO ESPECIFICO
    
@app.route('/aluno/<int:id>', methods=["GET"])
def visualizar_aluno(id):
    aluno = db.session.query(Alunos).filter(Alunos.id == id).scalar()

    return render_template('alunos/aluno.html', aluno = aluno)

# PAGINA PARA EDITAR ALUNO

@app.route('/aluno/<int:id>/editar', methods=["GET"])
def pagina_edicao(id):
    aluno = db.session.query(Alunos).filter(Alunos.id == id).scalar()
    return render_template('alunos/editar/editar_aluno.html', aluno = aluno)

# FUNÇÃO PARA EDITAR O ALUNO, SE DER TUDO CERTO ELE RETORNA PARA A ROTA DA PAGINA DE EDIÇÃO

@app.route('/aluno/<int:id>/editar_aluno', methods=["GET", "POST"])
def editar_aluno(id):
    
    aluno = db.session.query(Alunos).filter(Alunos.id == id).scalar()
    
    novo_nome = request.form.get('nome')
    novo_idade = request.form.get('idade')
    novo_telefone = request.form.get('telefone')
    nova_turma = request.form.get('turma')
    
    if aluno:
        aluno.nome = novo_nome
        aluno.idade = novo_idade
        aluno.telefone = novo_telefone
        aluno.turma = nova_turma
        db.session.commit()
        
        
    return redirect(f"/aluno/{aluno.id}")

# EDITAR OU ATRIBUIR NOTA AO ALUNO


@app.route('/aluno/<int:id>/notas')
def notas(id):
    aluno = db.session.query(Alunos).filter(Alunos.id == id).scalar()
    return render_template('alunos/editar/editar_notas.html', aluno = aluno)

@app.route('/aluno/<int:id>/editar_notas', methods=["GET", "POST"])
def editar_notas(id):
    aluno = db.session.query(Alunos).filter(Alunos.id == id).scalar()
    
    if aluno:
        aluno.portugues = int(request.form.get('portugues'))
        aluno.matematica = int(request.form.get('matematica'))
        aluno.geografia = int(request.form.get('geografia'))
        aluno.ciencias = int(request.form.get('ciencias'))
        aluno.ingles = int(request.form.get('ingles'))
        
        db.session.commit()
        
    return redirect(f"/aluno/{aluno.id}")
    
# DELETAR ALUNO 

@app.route('/aluno/<int:id>/deletar', methods=["GET"])
def deletar_aluno(id):
    aluno = db.session.query(Alunos).filter(Alunos.id == id).scalar()
    db.session.delete(aluno)
    db.session.commit()
    return redirect('/listar_alunos')
    
    
if __name__ == '__main__':
    app.run(debug=True)