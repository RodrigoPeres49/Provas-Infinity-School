from models import *
import os

os.system('cls')
#EXEMPLO DA DECLARAÇÃO DAS CLASSES E SUBCLASSES

print("Exemplo das classes e subclasses abaixo:")
print("Classe Pai:' Material ':")

# CLASSE MATERIAL

jornal = Material("Jornal Super", "Grupo Diario e Associados")

# EXIBIR INFORMAÇÕES DO MATERIAL
print("\n")
print(jornal.exibir_informacoes())

print("="*30)
os.system('pause')

# SUBCLASSES REVISTA E LIVRO
os.system('cls')

revista = Revista("Veja", "Editora Abril", "1º Edição")
livro = Livro("Programação Python", "Davi Lucciola" ,"Programação Full Stack")

print("SubClasses :' Livro e Revista ':")
os.system('pause')
os.system('cls')

# EXIBIR INFORMAÇÕES DAS SUBCLASSES

print("Livro:")
print("")
print(livro.exibir_informacoes())
print("="*30)


os.system('pause')
os.system('cls')

print("Revista:")
print("")
print(revista.exibir_informacoes())
print("="*30)
os.system('pause')
