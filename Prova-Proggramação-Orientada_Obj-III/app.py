from posto_combustivel import *
import os

# FUNÇÕES PARA PAUSAR E LIMPAR OS CAMPOS

def pause():
    os.system("pause")
def clear():
    os.system('cls')

# DEFININDO OS VEICULOS E OS TIPOS DE COMBUSTIVEL

veiculo = Veiculo("Fiat", "Siena 2013", 20, 48, 12)
combustiveis = [Combustivel("alcool", 4.09, 1000),Combustivel("gasolina", 5.99, 1000)]

# INICIANDO O MENU INTERATIVO

operador = None

while operador != "0":
    
    clear()
    print(f"Veiculo:{veiculo.modelo}\nCombustivel:{veiculo.bomba:.2f}")
    print("1- Para abastecer o veículo")
    print("2- Para simular uma corrida em km")
    print("3- Alterar valor do combustível")
    print("4- Alterar veículo")
    print("0- Para sair")
    operador = input("Digite uma opção: ")

    # OPÇÃO 1 ABASTECER O VEICULO:

    if operador == "1":
        clear()
        print('Selecione um tipo de combustível:')
        
        # PERCORRER A LISTA DE COMBUSTIVEIS
        
        for i, combustivel in enumerate(combustiveis, start=1):
            print(f"{i} - {combustivel.tipo} (R${combustivel.valor}/litro)")
            
        # DEFINIR O TIPO DE COMBUSTIVEL

        tipo = int(input('Digite o tipo de combustível: ')) -1
        
        if tipo in range(len(combustiveis)):
            
            tipo_combustivel = combustiveis[tipo]
            
            # DEFINIR O METODO DE ABASTECIMENTO SE VAI SER POR VALOR OU POR LITRO
            
            clear()
            print("1- Por valor\n2- Por litro")
            metodo_abastecimento = input("Digite o método de abastecimento: ")
            if metodo_abastecimento == "1":
                valor = float(input('Digite o valor a ser abastecido (R$): '))
                litros = tipo_combustivel.abastecer_valor(veiculo.bomba, valor)
                
                # VERIFICAR SE A QUANTIDADE DE LITROS VAI ULTRAPASSAR O LIMITE DA BOMBA DE GASOLINA
                
                if veiculo.abastecer_veiculo(litros) == False:
                    print(f"Quantidade de {litros:.2f} ultrapassou o limite da bomba de combustível")
                else:
                    veiculo.abastecer_veiculo(litros)
                    print(f"Veículo abastecido com {litros:.2f} litros de {tipo_combustivel.tipo} no valor de {valor:.2f}.")
                    
                    
            elif metodo_abastecimento == "2":
                litros = float(input('Digite quantos litros vão ser abastecidos: '))
                valor = tipo_combustivel.abastecer_litro(veiculo.bomba, litros)
                
                # VERIFICAR SE A QUANTIDADE DE LITROS VAI ULTRAPASSAR O LIMITE DA BOMBA DE GASOLINA
                
                if veiculo.abastecer_veiculo(litros) == False:
                    print(f"Quantidade de {litros:.2f} ultrapassou o limite da bomba de combustível")
                else:
                    veiculo.abastecer_veiculo(litros)
                    print(f"Veículo abastecido com {litros:.2f} litros de {tipo_combustivel.tipo} no valor de {valor:.2f}.")
                    
               
            else:
                print("Método Inválido.")
                
        else:
            print("Tipo de combustível inválido.")
        pause()
        
    # SIMULADOR DE CONSUMO POR LITRO
    
    elif operador == "2":
        clear()
        
        # DIGITAR O KM PARA SIMULAÇÃO
        
        km = float(input("Digite a distância da corrida em km: "))
        
        # CALCULAR COMBUSTIVEL NECESSARIO PARA VERIFICAR SE É POSSÍVEL A VIAJEM
        
        combustivel_necessario = km / veiculo.consumo
        
        if combustivel_necessario > veiculo.bomba:
            print("Combustível insuficiente para a corrida.")
            
        # SE O COMBUSTIVEL FOR NECESSARIO PARA A CORRIDA É CALCULADO O CONSUMO DE COMBUSTIVEL POR KM
        
        else:
            veiculo.bomba -= combustivel_necessario
            print(f"Corrida realizada. Combustível restante: {veiculo.bomba:.2f} litros.")
        pause()


    # 3 ALTERAR O VALOR DO COMBUSTIVEL
    
    elif operador == "3":
        clear()
        
        # SELECIONAR O TIPO DE COMBUSTIVEL PARA ALTERAR O VALOR
        
        print('Selecione um tipo de combustível para alterar o valor:')
        for i, combustivel in enumerate(combustiveis, start=1):
            print(f"{i} - {combustivel.tipo} (R${combustivel.valor}/litro)")
        
        # SELECIONAR O TIPO DE COMBUSTIVEL DESEJADO NA LISTA SE O MESMO DIGITAR 1 ELE IRÁ ATÉ O ELEMENTO 0 DA LISTA E VICE VERSA
        
        tipo = int(input('Digite o número do combustível desejado: ')) - 1
        
        # SELECIONANDO O VALOR CORRETO ELE ABRE O CAMPO PARA ALTERAR O VALOR DO COMBUSTIVEL ESCOLHIDO
        
        if tipo in range(len(combustiveis)):
            novo_valor = float(input('Digite o novo valor do combustível (R$): '))
            combustiveis[tipo].alterar_valor(novo_valor)
            print(f"Novo valor do {combustiveis[tipo].tipo} é R${novo_valor:.2f}.")
        else:
            print("Tipo de combustível inválido.")
        pause()

    # 4 ALTERAR VEICULO
    
    elif operador == "4":
        clear()
        
        # SE DESEJA MUDAR O VEICULO OU FAZER ALTERAÇÕES NO VEICULOS VOCÊ APENAS DIGITA OS DADOS DO MESMO ABAIXO
        
        # VERIFICAR SE OS DADOS DO VEICULOS SÃO COMPATIVEIS COM OS ELEMENTOS
        
        try:
            marca = input("Digite a marca do veículo: ")
            modelo = input("Digite o modelo do veículo: ")
            bomba = float(input("Digite a quantidade de combustível atual no veículo (litros): "))
            capacidade = float(input("Digite a capacidade total do tanque (litros): "))
            consumo = float(input("Digite o consumo do veículo (km/l): "))
        
            # SE SEGUIR CONFORME O PLANEJADO ELE APLICA AS ALTERAÇÕES
            
            veiculo = Veiculo(marca, modelo, bomba, capacidade, consumo)
            print("Veículo atualizado com sucesso.")
            pause()
        
        except ValueError:
            clear()
            print("Dados do veículo inválidos.")
            pause()
    
    # 0 ENCERRAR PROGRAMA
    
    elif operador == "0":
        print("Saindo...")
        pause()
        clear()
        break
    
    # OPÇÃO INVALIDA
    
    else:
        print("Opção inválida. Tente novamente.")
        pause()
