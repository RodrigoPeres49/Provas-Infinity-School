from tkinter import *
from tkinter import messagebox
from models import Base, Usuarios, Exercicios, db
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

# DEFINIR JANELA E BANCO DE DADOS

root = Tk()
Base.metadata.create_all(db)

# FUNÇÃO PARA CENTRALIZAR ELEMENTOS NO GRID

def centralizar_grid(janela, row_final, column_final):
    janela.rowconfigure(0, weight=1)
    janela.rowconfigure(row_final, weight=1)
    janela.columnconfigure(0, weight=1)
    janela.columnconfigure(column_final, weight=1)

# JANELA DE LOGIN

class Janela_Login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x480")
        self.frames()
        self.widgets()
        
        # CHAMAR FUNÇÃO PARA CENTRALIZAR O GRID
        
        centralizar_grid(self.root,2,2)
    
        
    def frames(self):
        self.frame1 = Frame(self.root, bg="lightgreen", width=560, height=450)
        self.frame1.grid(row=1, column=1)
        self.frame1.grid_propagate(False)
        centralizar_grid(self.frame1, 9, 3)
    
         
    def widgets(self):
        
        # TITULO
        
        titulo = Label(self.frame1, text="BEM VINDO", font=("Verdana", 20, "bold"), bg="lightgreen")
        titulo.grid(row=1, column=1, padx=10, pady=10, columnspan=2)
        
        # USUARIO
        
        
        usuario = Label(self.frame1, text="Usuario: ", font=("Verdana", 12, "bold"), bg="lightgreen")
        usuario.grid(row=2, column=1, padx=5, pady=5, columnspan=2)
        self.usuario_entry = Entry(self.frame1, width=50)
        self.usuario_entry.grid(row=3, column=1, padx=5, pady=5, columnspan=2)
        
        # SENHA
        
        
        senha = Label(self.frame1, text="Senha: ", font=("Verdana", 12, "bold"), bg="lightgreen")
        senha.grid(row=4, column=1, padx=5, pady=5, columnspan=2)
        self.senha_entry = Entry(self.frame1, width=50, show="*")
        self.senha_entry.grid(row=5, column=1, padx=5, pady=5, columnspan=2)
        
        # BOTOES PARA ENTRAR E CADASTRAR
        
        self.entrar = Button(self.frame1, text="ENTRAR", command=self.verificar_login)
        self.entrar.grid(row=6, column=1, padx=20, pady=20)
        self.cadastrar = Button(self.frame1, text="CADASTRAR", command=self.janela_cadastro)
        self.cadastrar.grid(row=6, column=2, padx=20, pady=20)
    
    
    # FUNCÃO PARA ABRIR JANELA DE CADASTRO
        
    def janela_cadastro(self):
        self.root.destroy()
        root = Tk()
        app = Janela_Cadastro(root)
        root.mainloop() 

    # FUNCAO PARA VERIFICAR O LOGIN
    
    def verificar_login(self):
        session = Session(db)
    
        usuario = self.usuario_entry.get()
        senha = self.senha_entry.get()
    
        try:
            usuario_db = session.query(Usuarios).filter(Usuarios.email == usuario).one()
            senha_db = session.query(Usuarios).filter(Usuarios.senha == senha).one()
        
            messagebox.showinfo("SUCESSO!", "REDIRECIONANDO PARA TELA DO USUARIO!")
            self.root.destroy()
            root = Tk()
            app = Janela_Usuario(root, usuario)
            root.mainloop() 
        except NoResultFound:
            messagebox.showwarning("ERRO!", "USUARIO OU SENHA INVALIDOS")

# JANELA DE CADASTRO AQUI ESTÃO AS CONDICIONAIS QUE ESTÃO PEDINDO NA PROVA >>>>
                                 
class Janela_Cadastro:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")
        self.frames()
        self.widgets()
        
        # CHAMAR FUNÇÃO PARA CENTRALIZAR O GRID
        
        centralizar_grid(self.root,2,2)
            
        
    def frames(self):
        self.frame1 = Frame(self.root, bg="lightgreen", width=760, height=550)
        self.frame1.grid(row=1, column=1)
        self.frame1.grid_propagate(False)
        centralizar_grid(self.frame1, 9, 3)
        
        
    def widgets(self):
        
        # TITULO
        
        titulo = Label(self.frame1, text="Cadastre-se", font=("Verdana", 20, "bold"), bg="lightgreen")
        titulo.grid(row=1, column=1, padx=10, pady=10, columnspan=2)
        
        # EMAIL
        
        
        usuario = Label(self.frame1, text="Email (Usuario): ", font=("Verdana", 12, "bold"), bg="lightgreen")
        usuario.grid(row=2, column=1, padx=5, pady=5, columnspan=2)
        self.email_entry = Entry(self.frame1, width=50)
        self.email_entry.grid(row=3, column=1, padx=5, pady=5, columnspan=2)
        
        # NOME 
        
        nome = Label(self.frame1, text="Nome Completo: ", font=("Verdana", 12, "bold"), bg="lightgreen")
        nome.grid(row=4, column=1, padx=5, pady=5, columnspan=2)
        self.nome_entry = Entry(self.frame1, width=50)
        self.nome_entry.grid(row=5, column=1, padx=5, pady=5, columnspan=2)
        
        # SENHA
        
        
        senha = Label(self.frame1, text="Senha: ", font=("Verdana", 12, "bold"), bg="lightgreen")
        senha.grid(row=6, column=1, padx=5, pady=5, columnspan=2)
        self.senha_entry = Entry(self.frame1, width=50)
        self.senha_entry.grid(row=7, column=1, padx=5, pady=5, columnspan=2)
        
        # ENTRAR E CADASTRAR
        
        self.entrar = Button(self.frame1, text="CADASTRAR", command=self.cadastrar_usuario)
        self.entrar.grid(row=8, column=1, padx=20, pady=20)
        self.cadastrar = Button(self.frame1, text="VOLTAR", command=self.voltar_tela_login)
        self.cadastrar.grid(row=8, column=2, padx=20, pady=20)
    
    
    def voltar_tela_login(self):
        self.root.destroy()
        root = Tk()
        app = Janela_Login(root)
        root.mainloop()     

    # FUNÇÃO PARA CADASTRAR O USUARIO >>>>    
    
    def cadastrar_usuario(self):
        with Session(db) as session:
            usuario = Usuarios(
                email = self.email_entry.get(),
                senha = self.senha_entry.get(),
                nome = self.nome_entry.get(),
                exercicios = []
                )
            
        # CONDICIONAL PARA VALIDAR O EMAIL OBS: AO INVES DE COLOCAR MENOR QUE 6 COLOQUEI MENOR QUE 10
            
        if len(self.email_entry.get()) < 10 or '@' not in self.email_entry.get() or '.' not in self.email_entry.get():
            return messagebox.showwarning("ERRO!", 'Digite um E-mail válido')
                
        else:
            session.add(usuario)
            session.commit()
            self.email_entry.delete(0, END)
            self.senha_entry.delete(0, END)
            self.nome_entry.delete(0,END)
            return messagebox.showinfo("SUCESSO", "Usuario Cadastrado com Sucesso!")

# JANELA DE USUARIO EM FASE DE TESTES      
        
class Janela_Usuario:
    
    def __init__(self, root, usuario):
        self.root = root
        self.usuario = usuario
        self.root.geometry("800x600")
        self.frames()
        self.widgets()
        centralizar_grid(self.root, 2, 2)
        
        
    def frames(self):
        self.frame1 = Frame(self.root, bg="lightgreen", width=760, height=550)
        self.frame1.grid(row=1, column=1)
        self.frame1.grid_propagate(False)
        centralizar_grid(self.frame1, 9, 3)
        
    def widgets(self): 
        
        
        titulo = Label(self.frame1, text=f"BEM VINDO ... {self.usuario} ... estamos em fase de testes...", font=("Verdana", 11, "bold"), bg="lightgreen")
        titulo.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

# INICIANDO PROGRAMA        
    
if __name__ == '__main__':
    app = Janela_Login(root)
    root.mainloop()
            
    