from flask import redirect, flash
from flask_login import LoginManager
from db import db
from models import Cliente
from sqlalchemy.orm import Mapped

login_manager = LoginManager()

@login_manager.user_loader
def carregar_usuario(id:Mapped[int]) -> Cliente:
    return db.session.query(Cliente).get(id)

@login_manager.unauthorized_handler
def unauthorized_handler():
    flash('Usuario ou senha inválidos', category='error')
    return redirect('/')