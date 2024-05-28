import os

lista = []
contagem  = 10
pares = ()
impares = ()

while contagem != 0:
    os.system('cls')
    print(lista)
    numero = int(input('Insira dez valores na lista: '))
    lista.append(numero)
    contagem -= 1

os.system('cls')    
    
selecao = 1

while selecao != 0:
    print(lista)
    selecao = int(input('- Digite 1 para exibir numeros pares e impares em listas diferentes\n- Digite 2 para somar os valores da lista :\n'))   
    if selecao == 1:
        lista_pares = []
        lista_impares = []
        for i in lista:
            if i % 2 == 0:
                lista_pares.append(i)
            else:
                lista_impares.append(i)
        
        pares = lista_pares
        impares = lista_impares
        
        os.system('cls')
        print('Numeros Pares: ',pares,'\nNumeros Impares: ',impares)
        os.system('pause')
        os.system('cls')
        
    elif selecao == 2:
        os.system('cls')
        print(lista)
        print('A soma dos valores é igual a ',sum(lista))
        os.system('pause')
        os.system('cls')
    elif selecao == 0:
        break
    else: 
        os.system('cls')
        print(lista)
        print('Por favor insira um valor valido.')
        os.system('pause')
        os.system('cls')  
                
os.system('cls')
print('Programa encerrado!')
os.system('pause')

