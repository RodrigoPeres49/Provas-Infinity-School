from db import db
from sqlalchemy import ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin


class Cliente(db.Model, UserMixin):

    # TABELA CLIENTES
        
    __tablename__ = 'clientes'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    
    # DADOS DO CLIENTE
    
    usuario: Mapped[str] = mapped_column(unique=True, nullable=False)
    senha: Mapped[str] = mapped_column(nullable=False)
    nome: Mapped [str]
    email: Mapped[str] = mapped_column(unique=True)
    cpf: Mapped[str]
    
    # DINHEIRO FICTICIO PARA COMPRAR OS PRODUTOS
    
    dinheiro_ficticio: Mapped[float]
    
    # RELACIONAMENTO COM A TABELA PRODUTOS
    
    produtos: Mapped[list["Produto"]] = relationship("Produto", back_populates="cliente")
    
    # CONSTRUTOR DO OBJETO
    
    def __init__(self, usuario, senha, nome, email, cpf, dinheiro_ficticio):
        self.usuario = usuario
        self.senha = generate_password_hash(senha)
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.dinheiro_ficticio = dinheiro_ficticio
        
    # FUNÇÃO PARA VERIFICAR A SENHA
    
    def verificar_senha(self, senha_digitada: str)-> bool:
        return check_password_hash(self.senha, senha_digitada)
    
    
class Produto(db.Model):
    
    __tablename__ = 'produtos'
    
    # DADOS DO PRODUTO
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(unique=True, nullable=False)
    descricao: Mapped[str] = mapped_column(nullable=False)
    preco: Mapped[float]
    
    # CONDIÇÃO PARA VER SE ELE FOI VENDIDO OU NÃO
    
    vendido: Mapped[bool] = mapped_column(default=False)
    
    # RELACIONAMENTO COM O CLIENTE QUE ESTÁ VENDENDO O PRODUTO
   
    cliente_id: Mapped[int] = mapped_column(ForeignKey("clientes.id"), nullable=False)
    cliente: Mapped["Cliente"] = relationship("Cliente", back_populates="produtos")
    
    def __init__(
        self,
        nome:str, descricao:str, preco:float, cliente_id:int, vendido:bool
        )-> None:
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.cliente_id = cliente_id
        self.vendido = vendido
        
        
        
        
        
    