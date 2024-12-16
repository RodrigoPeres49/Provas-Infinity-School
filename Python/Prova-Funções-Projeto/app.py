from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column , DeclarativeBase

class Base(DeclarativeBase):
    pass
db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tarefas.db"

db.init_app(app)

class Tarefas(db.Model):
    id : Mapped[int] = mapped_column(primary_key=True)
    nome : Mapped[str] = mapped_column(unique=True)
    descricao : Mapped[str]

@app.route("/")
def index():
    return redirect("/listar")

@app.route("/listar")
def listar():
    tarefas = db.session.execute(db.select(Tarefas).order_by(Tarefas.nome)).scalars()
    return render_template('index.html', tarefas = tarefas)

@app.route("/criar_tarefa", methods=["GET", "POST"])
def criar_tarefa():
    if request.method == "POST":
        tarefa = Tarefas(
            nome = request.form["nome"],
            descricao = request.form["descricao"]
        )
        db.session.add(tarefa)
        db.session.commit()
        return redirect("/listar")
    return(render_template("criar_tarefa.html"))
    
@app.route("/tarefa/<int:id>/")
def detalhes_tarefa(id):
    tarefa = db.get_or_404(Tarefas, id)
    return render_template('detalhes.html', tarefa = tarefa)

@app.route("/tarefa/<int:id>/apagar")
def apagar_tarefa(id):
    
    tarefa = db.get_or_404(Tarefas, id)
    db.session.delete(tarefa)
    db.session.commit()
    
    return redirect(url_for("listar"))

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
