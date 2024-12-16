from flask import render_template, redirect, Blueprint, request, flash
from models import *
from db import db

posto_bp = Blueprint("Combustivel", __name__)

# ADICIONANDO ALGUNS VEÍCULOS AO BANCO DE DADOS



@posto_bp.route("/")
def pagina_inicial():
    return render_template('simulador_posto.html')

@posto_bp.route("/veiculo/<int:id>", methods="POST")
def selecionar_veiculo(id):
    veiculo = db.session.query(Veiculo).where(Veiculo.id == id).first()
    return render_template("simulador_posto.html", veiculo = veiculo)

@posto_bp.route("/abastecer<int:id>", methods=["POST"])
def abastecer(id):
    combustivel = db.session.query(Combustivel).filter(Combustivel.tipo == 'alcool', Combustivel.tipo == 'flex')
    veiculo = db.session.query(Veiculo).where(Veiculo.id == id)
    metodo = request.form.get('metodo-pagamento')
    tipo_combustivel = request.form.get('tipo')
    if tipo_combustivel == 'alcool' or tipo_combustivel == 'flex':
        if veiculo.tipo_combustivel == 'alcool' or tipo_combustivel == 'flex':
            if metodo == 'dinheiro':
                combustivel.abastecer_valor(veiculo.bomba, metodo)
            else:
                combustivel.abastecer_litro(veiculo.bomba, metodo)
        
        
    
    
                                   