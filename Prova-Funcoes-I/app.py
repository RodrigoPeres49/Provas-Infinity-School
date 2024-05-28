import os

os.system('cls')

def relatorio_aluno(aluno, nota):
    
    aluno = input('Digite o nome do aluno: ')
    
    nota.append(int((input('Digite a nota de Português: '))))
    nota.append(int(input('Digite a nota de Matemática: ')))
    nota.append(int(input('Digite a nota de Geografia: ')))
    nota.append(int(input('Digite a nota de Ciências: ')))
    nota.append(int(input('Digite a nota de Inglês: ')))
    os.system('cls')
    return print('Aluno', aluno ,'\nNota Português: ', nota[0] ,'\nNota Matemática: ', nota[1] ,'\nNota Geografia: ', nota[2] ,'\nNota Ciências: ', nota[3] ,'\nNota Inglês : ', nota[4])
    
def verificar_media(nota, situacao):
    soma = sum(nota)
    media = soma/len(nota)
    situacao = ''
    if media >= 5:
        situacao = 'Aprovado'
    else:
        situacao = 'Reprovado'
        
    return print('Media das notas: ', media, '\nSituação: ',situacao)
    
aluno = ''
nota = []
situacao = ''

relatorio_aluno(aluno, nota)
verificar_media(nota, situacao)
os.system('pause')
os.system('cls')





        

