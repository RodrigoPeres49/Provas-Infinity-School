
# CLASSE COMBUSTIVEL

class Combustivel:
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
    # INFORMA O PAGAMENTO A SER FEITO E É SOMADO POR LITROS DE ACORDO COM O PREÇO DO LITRO
    
    def abastecer_valor(self, bomba, pagamento):
         
        litro = pagamento / self.valor
        self.tanque = self.tanque - litro
        bomba += litro
        return litro
    
    # FUNÇÃO PARA ABASTECER POR LITRO
    # INFORMA OS LITROS A SEREM COLOCADO NO VEICULO E DEPOIS RETORNA O VALOR EM PAGAMENTO DE ACORDO COM O VALOR DO LITRO
    
    def abastecer_litro(self, bomba ,litro):
        
        pagamento = litro * self.valor
        self.tanque = self.tanque - litro
        bomba += litro
        return pagamento


# CLASSE VEICULO

class Veiculo:
            
        def __init__(self, marca:str, modelo:str, bomba:float, capacidade:float, consumo:float):
            self.marca = marca
            self.modelo = modelo
            self.bomba = bomba
            self.capacidade = capacidade
            self.consumo = consumo
        
        
        def abastecer_veiculo(self, combustivel):
            limite_bomba = self.capacidade - self.bomba
            if combustivel > limite_bomba:
                return False
            else:
                self.bomba += combustivel
                return self.bomba
        
        