from flask import render_template, redirect, Blueprint, request, flash
from models import *
import flask_login as fl
from db import db

produto_bp = Blueprint("Produto", __name__)

# PÁGINA INICIAL

@produto_bp.route("/", methods=["GET"])
def root():
    return redirect('/login')

# OPERAÇÕES DE COMPRA E VENDA EM GERAL

# PAGINA PARA COLOCAR UM PRODUTO A VENDA

@produto_bp.route("/produto/vender", methods=["GET"])
def pag_adicionar_produto():
    usuario: Cliente = fl.current_user
    return render_template("produtos/venda.html", usuario = usuario)

# ADICIONAR PRODUTO A VENDA

@produto_bp.route("/produto/vender", methods=["POST"])
def adicionar_produto():
    
    usuario: Cliente = fl.current_user
    form_data = dict(request.form)
    
    produto = Produto(
        form_data.get("nome"),
        form_data.get("descricao"),
        form_data.get("preco"),
        usuario.id,
        False
    )
    
    db.session.add(produto)
    db.session.commit()
    
    return redirect("/cliente")

#LISTAR PRODUTOS POSTADOS PELO PRÓPRIO USUARIO

@produto_bp.route('/produto/meus_produtos')
def listar_produtos_usuario():
    usuario : Cliente = fl.current_user
    produtos = db.session.query(Produto).where(Produto.cliente_id == usuario.id)
    return render_template('/produtos/meus_produtos.html', usuario = usuario, produtos = produtos)

# LISTAR PRODUTOS A VENDA

@produto_bp.route("/produto/lista")
def listar_produtos_compra():
    usuario : Cliente = fl.current_user
    produtos = db.session.query(Produto).filter(Produto.cliente_id != usuario.id, Produto.vendido == False)
    return render_template('/produtos/compras.html', usuario = usuario, produtos = produtos)

# COMPRAR PRODUTO

@produto_bp.route("/produto/comprar/<int:id>")
def comprar_produto(id):
    usuario: Cliente = fl.current_user
    produto = db.session.query(Produto).where(Produto.id == id).first()
    
    
    if produto is None:
        flash('Produto não encontrado.')
        return redirect('/produto/lista')
    
    vendedor = db.session.query(Cliente).where(Cliente.id == produto.cliente_id).first()
    
    if vendedor is None:
        flash('Vendedor não encontrado.')
        return redirect('/produto/lista')
    
    if usuario.dinheiro_ficticio >= produto.preco:
        try:
            produto.vendido = True
            usuario.dinheiro_ficticio -= produto.preco
            db.session.commit()
        except ValueError:
            flash('Erro ao processar a compra.')
            return redirect('/produto/lista')
        
        if produto.vendido:
            vendedor.dinheiro_ficticio += produto.preco
            db.session.commit()
        
        return redirect('/produto/lista')
    else:
        flash('Créditos insuficientes.')
        return redirect('/produto/lista')

    
    


    
    

