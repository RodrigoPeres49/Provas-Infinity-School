import os
lista_numeros = []

while True:

    numero = (int(input('Digite um número para adicionar a lista: \nDigite 0 para encerrar.\nDigite o número ao lado: ')))
    if numero == 0:
        os.system("cls")
        print('----------------------RELATÓRIO----------------------')
        elementos = len(lista_numeros)
        print('O numero de elementos adicionados a lista é igual: ', elementos)
        soma = sum(lista_numeros)
        print('A soma de todos os elementos é igual: ', soma)
        print('A média aritmetica dos elementos é igual a:', soma/elementos)
        break
    else:
        lista_numeros.append(numero)
        os.system("cls")
        print('Numeros adicionados a lista: ', lista_numeros,'\n')
    


    