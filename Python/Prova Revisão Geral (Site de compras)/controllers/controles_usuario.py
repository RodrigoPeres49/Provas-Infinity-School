from flask import render_template, redirect, Blueprint, request, flash
import flask_login as fl
from models import *
from db import db 

# TAREFAS DO USUARIO

cliente_bp = Blueprint("Cliente", __name__)

# LOGIN

# ABRE A PÁGINA DE LOGIN

@cliente_bp.route("/login", methods=["GET"])
def pagina_login():
    usuario = ''
    return render_template('index.html', usuario = usuario)

# VERIFICAR LOGIN COM O MESMO ENDEREÇO MAS O MÉTODO POST

@cliente_bp.route("/login", methods = ["POST"])
def login():
    form_data = dict(request.form)
    
    usuario = form_data.get('usuario')
    senha = form_data.get('senha')
    
    cliente = db.session.query(Cliente).where(Cliente.usuario == usuario).first()
    
    # VERIFICAR SE O USUARIO E A SENHA ESTÃO CORRETOS
    
    if cliente is None or not cliente.verificar_senha(senha):
        flash('Usuario ou senha inválidos.', category='error')
        return redirect('/login')
    
    fl.login_user(cliente)
    return redirect('/cliente')

# LOGOUT

# FUNÇÃO PARA DESLOGAR

@cliente_bp.route("/logout", methods= ["GET"])
@fl.login_required
def logout():
    fl.logout_user()
    return redirect('/login')

# PÁGINA DO CLIENTE

@cliente_bp.route('/cliente', methods=["GET"])
@fl.login_required
def cliente():
    usuario: Cliente = fl.current_user
    return render_template('cliente/cliente.html', usuario = usuario)

# CADASTRO  

@cliente_bp.route("/cadastro", methods=["GET"])
def pagina_cadastro():
    usuario = ''
    return render_template("cliente/cadastro.html", usuario = usuario)

# FUNÇÃO PARA ENVIAR DADOS DO CADASTRO E VERIFICAR O CADASTRO

@cliente_bp.route("/cadastro", methods= ["POST"])
def cadastro():
    form_data = dict(request.form)
    
    usuario = form_data.get('usuario')
    senha = form_data.get('senha')
    confirmar_senha = form_data.get('confirmar-senha')
    nome = form_data.get('nome')
    email = form_data.get('email')
    cpf = form_data.get('cpf')
    
    # NO FORMULÁRIO DE CADASTRO IRÁ CONTER DOIS CAMPOS DE SENHA E OS VALORES TEM QUE SER IGUAIS
    
    if senha != confirmar_senha:
        flash('Senhas diferentes, favor verificar novamente.', category='error')
        return redirect('/cadastro')
    
    # VERIFICAR SE JÁ EXISTE UM CADASTRO COM O NOME DE USUARIO QUE O CLIENTE QUER CADASTRAR
    
    cliente_existente = db.session.query(Cliente).where(Cliente.usuario == usuario).first()
    
    if cliente_existente:
        flash('Usuario já existe', category='error')
        return redirect('/cadastro')
    
    cliente = Cliente(usuario, senha, nome, email, cpf, dinheiro_ficticio= 0)
    db.session.add(cliente)
    db.session.commit()
    
    flash('Usuario cadastrado com sucesso!', category='success')
    return redirect('/login')


# ADICIONAR DINHEIRO FICTICIO

@cliente_bp.route('/add', methods=["GET"])
def pagina_dinheiro_ficticio():
    usuario: Cliente = fl.current_user
    return render_template('cliente/creditos.html', usuario = usuario)

    
@cliente_bp.route('/add', methods=["POST"])
def add_dinheiro_ficticio():
    valor = request.form.get('dinheiro_ficticio')
    usuario: Cliente = fl.current_user
    usuario.dinheiro_ficticio = usuario.dinheiro_ficticio + float(valor)
    db.session.commit()
    
    return redirect('/cliente')