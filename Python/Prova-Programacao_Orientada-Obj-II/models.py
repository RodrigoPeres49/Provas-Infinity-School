
# CLASSE MATERIAL

class Material:
    def __init__(self, titulo, autor_ou_editora):
        self.titulo = titulo
        self.autor_ou_editora = autor_ou_editora
    
    # METODO PARA EXIBIR AS INFORMAÇÕES
    
    def exibir_informacoes(self):
        
        # A VARIÁVEL " info " RECEBERA UMA STRING CONTENDO O VALOR DAS VARIAVEIS
        
        info = f"Obra: {self.titulo}\nFeito por: {self.autor_ou_editora}"
        
        # AQUI ESTÁ UMA CONDIÇÃO QUE NO CASO SE TIVER UMA VARIAVEL A MAIS NO CONSTRUTOR DA CLASSE
        # ELE ADICIONE UM CONTEUDO EXTRA AO STRING AONDE TERÁ OUTRO CAMPO REFERENTE AO NOME DA OUTRA VARIAVEL        
        for i, outro in vars(self).items():
            if i not in['titulo', 'autor_ou_editora']:
                info +=f"\n{i.capitalize()}: {outro}"
                
        # AO FAZER A VERIFICAÇÃO ELE RETORNA AS INFORMAÇÕES
        
        return info
    
# SUBCLASSES LIVRO E REVISTA ABAIXO
    
class Livro(Material):
    def __init__(self, titulo, autor_ou_editora, genero):
        super().__init__(titulo, autor_ou_editora)
        self.genero = genero
        
    
class Revista(Material):
    def __init__(self, titulo, autor_ou_editora ,edicao):
        super().__init__(titulo, autor_ou_editora)
        self.edicao = edicao
    
    
    