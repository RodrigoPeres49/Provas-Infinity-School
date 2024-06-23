class Elevador:
    def __init__(self, andares:list,pessoas:int, capacidade:int ):
        self.andares = andares
        self.pessoas = pessoas
        self.capacidade = capacidade
        
        # VALOR PADRÃO DE PESSOAS É IGUAL A 0 IDENPENDENTEMENTE AO DECLARAR OBJETO 
        # ELEVADOR E COLOCAR QUALQUER NUMERO NO CAMPO PESSOAS
        
        self.pessoas = 0
    
    # FUNÇÕES PARA DESCER E SUBIR
    
    # SE O ELEVADOR ESTIVER NA ULTIMA POSIÇÃO RETORNA COMO FALSO A FUNÇÃO
        
    def subir(self, posicao):
        if posicao >= len(self.andares) - 1:
            print("Você está no último andar.")
            return posicao
        else:
            print("subindo...")
            return posicao + 1
    
    # SE ESTIVER NA PRIMEIRA RETORNA COMO FALSO
    
    def descer(self, posicao):
        if posicao <= 0:
            print("Você está no primeiro andar.")
            return posicao 
        else:
            print("descendo...")
            return posicao - 1
    
    # ENTRAR PESSOAS
       
    def entrar_pessoas(self, acessos):
        
        # VERIFICA A CAPACIDADE ATUAL DO ELEVADOR
        
        capacidade_atual = self.capacidade - self.pessoas
        
        # SE A CAPACIDADE EXCEDER RETORNA COMO FALSO
        
        if acessos > capacidade_atual:
            print("Capacidade excedida!")
            return False
        else:
            self.pessoas += acessos
            return self.pessoas
    
    # LIBERAR SAIDA DE PESSOAS
    
    def sair_pessoas(self, saidas):
        
        # SE O NUMERO DE SAIDAS FOR MAIOR QUE O NUMERO DE PESSOAS NO ELEVADOR TEMOS UMA MENSAGEM DE ERRO.
        
        if saidas > self.pessoas:
            print("Não há pessoas suficientes no elevador!")
            return False
        else:
            self.pessoas -= saidas
            return self.pessoas