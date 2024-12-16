import os
from functools import reduce

# FUNÇÃO PARA PEGAR OS VALORES NA LISTA

def atribuir_valores(lista):
    for i in range(0,10):
        os.system('cls')
        print(lista)
        lista.append(int(input('Digite 10 valores na lista: ')))
        os.system('cls')
    return print('Lista adiquirida : ',lista), os.system('pause')

# VARIAVEIS

numeros = []
seletor = 10

atribuir_valores(numeros)
os.system('cls')

while seletor != 0:
    
# SELECIONAR OPÇÃO

    seletor = int(input('''Selecione uma opção:
1 - Obter uma lista com o quadrado de cada valor na lista atual.
2- Obter somente os numeros pares.
3- Somar todos os numeros da lista.
0- Sair
'''))
####################################################################
    
    # QUADRADO DE TODOS OS VALORES NA LISTA
    
    if seletor == 1:
        os.system('cls')
        resultado = list(map(lambda x: x**2, numeros))
        print(resultado)
        os.system('pause')
        os.system('cls')
        
    # SOMENTE OS NUMEROS PARES
    
    elif seletor == 2:
        os.system('cls')
        resultado = list(filter(lambda x: x%2 == 0, numeros))
        print(resultado)
        os.system('pause')
        os.system('cls')
        
    # SOMA DE TODOS OS VALORES NA LISTA
        
    elif seletor == 3:
        os.system('cls')
        resultado = reduce(lambda x, y: x + y, numeros)
        print(resultado)
        os.system('pause')
        os.system('cls')
        
    # ENCERRAR PROGRAMA
    
    elif seletor == 0:
        os.system('cls')
        print('Voce saiu')
        os.system('pause')
        os.system('cls')

    