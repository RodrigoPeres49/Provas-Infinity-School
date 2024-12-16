from models import *
import os

def limpar():
    os.system('cls')

def pausar():
    os.system('pause')
    

elevador = Elevador(["Térreo", "1 andar", "2 andar", "3 andar"], 0, 6)

operador = None

posicao_atual = 0
andar_atual = elevador.andares[posicao_atual]

while operador != '0':
    limpar()
    print(f"Andar: {andar_atual}")
    print(f"Pessoas: {elevador.pessoas}")
    print("1- Selecionar andar desejado")
    print("2- Subir um andar")
    print("3- Descer um andar")
    print("4- Liberar entrada de pessoas")
    print("5- Liberar saída de pessoas")
    print("0- Encerrar Programa")
    operador = input("Digite uma operação para o elevador: ")
    
    # 1 ESCOLHER O ANDAR DESEJADO
    
    if operador == '1':
        limpar()
        print("Andares disponíveis:", elevador.andares)
        
        # DIGITAR O ANDAR DESEJADO
        
        andar = int(input(f"Digite o número do andar desejado (0 a {(len(elevador.andares) - 1)}): "))
        if andar == posicao_atual:
            print('Você já está neste andar.')
            
        # VERIFICA SE O ANDAR É MAIOR OU IGUAL A PRIMEIRA POSIÇÃO E MENOR QUE A ULTIMA
        
        elif andar >=0 and andar < len(elevador.andares):
            
            # ENQUANTO O ANDAR NÃO FOR O DESEJADO ELE VAI REPEDIR AS FUNÇÕES DE DESCER OU SUBIR ATÉ O ANDAR DESEJADO
            
            while posicao_atual != andar:
                if posicao_atual < andar:
                    posicao_atual = elevador.subir(posicao_atual)
                    andar_atual = elevador.andares[posicao_atual]
                else:
                    posicao_atual = elevador.descer(posicao_atual)
                    andar_atual = elevador.andares[posicao_atual]
        else:
            print("Andar inválido!")
        pausar()
        
    # 2 SUBIR UM ANDAR

    elif operador == '2':
        limpar()
        posicao_atual = elevador.subir(posicao_atual)
        andar_atual = elevador.andares[posicao_atual]
        pausar()
        
    # 3 DESCER UM ANDAR
    
    elif operador == '3':
        limpar()
        posicao_atual = elevador.descer(posicao_atual)
        andar_atual = elevador.andares[posicao_atual]
        pausar()
        
    # 4 ENTRADA DE PESSOAS
    
    elif operador == '4':
        limpar()
        
        # DIGITAR O NUMERO DE PESSOAS QUE DESEJAM ENTRAR SE FOR MAIOR QUE A CAPACIDADE NÃO SERÁ PERMITIDA A ENTRADA
        
        acessos = int(input("Digite o número de pessoas que desejam entrar: "))
        if elevador.entrar_pessoas(acessos) is not False:
            print(f"{acessos} pessoas entraram.")
        pausar()
    
    # 5 SAIDA DE PESSOAS
        
    elif operador == '5':
        limpar()
        
        # SE O COMANDO DE SAIDA DE PESSOAS FOR MAIOR QUE O NUMERO TEMOS UMA MENSAGEM DE ERRO.
        
        saidas = int(input("Digite o número de pessoas que desejam sair: "))
        if elevador.sair_pessoas(saidas) is not False:
            print(f"{saidas} pessoas saíram.")
        pausar()

limpar()
print("Programa Encerrado.")        
pausar()
limpar()


        
        
                    
    
