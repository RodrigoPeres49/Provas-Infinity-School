from db import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
           

class Veiculo(db.Model):
    __tablename__ = 'veiculos'
    
    # DADOS DO VEÍCULO 
    
    id: Mapped[int] = mapped_column(primary_key=True)
    marca:Mapped[str]
    modelo:Mapped[str]
    
    # TIPO DE COMBUSTIVEL, CONSUMO POR KM E DUAS VARIAVEIS NOMEADAS COMO " bomba " QUE IRÁ SER O TANQUE DA GASOLINA
    # E A VARIÁVEL " capacidade " AONDE VAI SER O CAPACIDADE DE COMBUSTIVEL QUE O VEICULO IRA SUPORTAR
    
    tipo_combustivel: Mapped[str]
    bomba: Mapped[float]
    capacidade: Mapped[float]
    consumo: Mapped[float]
    
    def __init__(self, marca:str, modelo:str, tipo_combustivel:str, bomba:float, capacidade:float, consumo:float):
        self.marca = marca
        self.modelo = modelo
        self.tipo_combustivel = tipo_combustivel
        self.bomba = bomba
        self.capacidade = capacidade
        self.consumo = consumo
        
    def consumo_por_litro(self, km):
        combustivel_gasto = km / self.consumo
        if combustivel_gasto > bomba:
            return False
        else:
            bomba = bomba - combustivel_gasto
            return bomba
    
    def abastecer_veiculo(self, combustivel):
        limite_bomba = self.capacidade - self.bomba
        if combustivel > limite_bomba:
            return False
        else:
            self.bomba += combustivel
            return self.bomba

class Combustivel(db.Model):
    
    __tablename__ = 'combustivel'
    
    id:Mapped[int] = mapped_column(primary_key=True)
    tipo:Mapped[str] = mapped_column(unique=True)
    valor: Mapped[float]
    tanque: Mapped[float]
    
    
    def __init__(self, tipo: str, valor: float, tanque:float):
        self.tipo = tipo
        self.valor = valor
        self.tanque = tanque
        
    # REABASTECER TANQUE DO POSTO
    
    def abastecer_tanque(self, litro: float) -> float:
        self.tanque += litro
        return self.tanque
    
    # FUNÇÃO PARA ALTERAR O VALOR DO COMBUSTÍVEL
    
    def alterar_valor(self,novo_valor):
        
        # O VALOR ANTIGO VAI RECEBER O NOVO VALOR NA VARIÁVEL " novo_valor "
        
        self.valor = novo_valor
        return self.valor
        
        
    
    # FUNÇÃO PARA ABASTECER POR VALOR    
        
    def abastecer_valor(self, bomba:Veiculo.bomba, pagamento, litro):
        
        # RETORNA O PAGAMENTO A SER FEITO E ADICIONA O VALOR DO LITRO ABASTECIDO A VARIAVEL BOMBA
        
        valor = self.valor
        pagamento = valor * litro
        self.tanque = self.tanque - litro
        bomba = bomba + litro
        return pagamento
    
    # FUNÇÃO PARA ABASTECER POR LITRO
    
    def abastecer_litro(self, bomba:Veiculo.bomba ,litro, pagamento):
        
        # RETORNA O PAGAMENTO A SER FEITO E ADICIONA O VALOR DO LITRO ABASTECIDO A VARIAVEL BOMBA
        
        litro = self.tanque
        pagamento = self.valor * litro
        self.tanque = self.tanque - litro
        bomba = bomba + litro
        return pagamento
    