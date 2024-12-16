from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, Table
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship, sessionmaker

class Base(DeclarativeBase):
    pass

# Associação entre Membro e Livro
livro_membro_association = Table('livro_membro', Base.metadata,
    Column('livro_id', Integer, ForeignKey('livros.id')),
    Column('membro_id', Integer, ForeignKey('membros.id'))
)

class Biblioteca(Base):
    __tablename__ = 'bibliotecas'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    endereco = Column(String, nullable=False)
    livros = relationship('Livro', back_populates='biblioteca')
    membros = relationship('Membro', back_populates='biblioteca')

class Livro(Base):
    __tablename__ = 'livros'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    descricao = Column(String)
    emprestado = Column(Boolean, default=False)
    data_emprestimo = Column(String(15))
    data_devolucao = Column(String(15))
    biblioteca_id = Column(Integer, ForeignKey('bibliotecas.id'))
    biblioteca = relationship('Biblioteca', back_populates='livros')
    membros = relationship('Membro', secondary=livro_membro_association, back_populates='livros')

class Membro(Base):
    __tablename__ = 'membros'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    endereco = Column(String, nullable=False)
    biblioteca_id = Column(Integer, ForeignKey('bibliotecas.id'))
    biblioteca = relationship('Biblioteca', back_populates='membros')
    livros = relationship('Livro', secondary=livro_membro_association, back_populates='membros')
    historico = Column(String)  # Armazena o histórico de livros emprestados como uma string

# Configuração do banco de dados (SQLite, por exemplo)
engine = create_engine('sqlite:///biblioteca.db')
Base.metadata.create_all(engine)

# Criar uma sessão
Session = sessionmaker(bind=engine)
session = Session()



    