from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from typing import List, Optional
from sqlalchemy import create_engine

db = create_engine("sqlite:///usuarios.db", echo=True)

# BANCO DE DADOS

class Base(DeclarativeBase):
    pass

# TABELA USUARIOS

class Usuarios(Base):
    __tablename__ = 'usuarios'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(30))
    nome: Mapped[Optional[str]]
    senha: Mapped[str]
    
    exercicios: Mapped[List["Exercicios"]] = relationship(back_populates="usuario", cascade="all, delete-orphan")

# TABELA EXERCICIOS EM FASE DE TESTE

class Exercicios(Base):
    __tablename__ = 'exercicios'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    series: Mapped[str]
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))
    
    usuario: Mapped["Usuarios"] = relationship(back_populates="exercicios")
    
    
