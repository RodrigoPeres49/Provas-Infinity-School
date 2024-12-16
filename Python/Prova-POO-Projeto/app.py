import tkinter as tk
from tkinter import ttk, messagebox
from sqlalchemy.orm import sessionmaker
from models import Biblioteca, Livro, Membro, engine
from datetime import date
from tkcalendar import DateEntry

# Configurar a sessão do SQLAlchemy
Session = sessionmaker(bind=engine)
session = Session()

class BibliotecaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Biblioteca")
        self.biblioteca_dict = {}
        self.livro_dict = {}
        self.membro_dict = {}
        self.create_widgets()

    def create_widgets(self):
        # Botões de Ação
        tk.Button(self, text="Cadastrar Biblioteca", command=self.cadastrar_biblioteca).grid(row=0, column=0)
        tk.Button(self, text="Cadastrar Livro", command=self.cadastrar_livro).grid(row=0, column=1)
        tk.Button(self, text="Cadastrar Membro", command=self.cadastrar_membro).grid(row=0, column=2)
        tk.Button(self, text="Listar Livros por Biblioteca", command=self.listar_livros).grid(row=0, column=3)
        tk.Button(self, text="Gerar Empréstimo de Livro", command=self.gerar_emprestimo).grid(row=0, column=4)
        tk.Button(self, text="Devolver Livro", command=self.devolver_livro).grid(row=0, column=4)
        tk.Button(self, text="Listar Bibliotecas", command=self.listar_bibliotecas).grid(row=0, column=5)
        
    def update_biblioteca_dict(self):
        self.biblioteca_dict = {b.nome: b.id for b in session.query(Biblioteca).all()}

    def update_livro_dict(self):
        self.livro_dict = {l.nome: l.id for l in session.query(Livro).all()}

    def update_membro_dict(self):
        self.membro_dict = {m.nome: m.id for m in session.query(Membro).all()}

    def cadastrar_biblioteca(self):
        def submit():
            nome = nome_entry.get()
            endereco = endereco_entry.get()
            if nome and endereco:
                biblioteca = Biblioteca(nome=nome, endereco=endereco)
                session.add(biblioteca)
                session.commit()
                self.update_biblioteca_dict()  # Atualiza o dicionário de bibliotecas
                messagebox.showinfo("Sucesso", "Biblioteca cadastrada com sucesso!")
                popup.destroy()
            else:
                messagebox.showwarning("Atenção", "Por favor, preencha todos os campos.")

        popup = tk.Toplevel(self)
        popup.title("Cadastrar Biblioteca")

        tk.Label(popup, text="Nome:").grid(row=0, column=0)
        nome_entry = tk.Entry(popup)
        nome_entry.grid(row=0, column=1)

        tk.Label(popup, text="Endereço:").grid(row=1, column=0)
        endereco_entry = tk.Entry(popup)
        endereco_entry.grid(row=1, column=1)

        tk.Button(popup, text="Cadastrar", command=submit).grid(row=2, column=0, columnspan=2)

    def cadastrar_livro(self):
        def submit():
            nome = nome_entry.get()
            descricao = descricao_entry.get()
            biblioteca_nome = biblioteca_combo.get()
            biblioteca_id = self.biblioteca_dict.get(biblioteca_nome)
            if nome and descricao and biblioteca_id:
                livro = Livro(nome=nome, descricao=descricao, biblioteca_id=biblioteca_id)
                session.add(livro)
                session.commit()
                self.update_livro_dict()  # Atualiza o dicionário de livros
                messagebox.showinfo("Sucesso", "Livro cadastrado com sucesso!")
                popup.destroy()
            else:
                messagebox.showwarning("Atenção", "Por favor, preencha todos os campos.")

        popup = tk.Toplevel(self)
        popup.title("Cadastrar Livro")

        tk.Label(popup, text="Nome:").grid(row=0, column=0)
        nome_entry = tk.Entry(popup)
        nome_entry.grid(row=0, column=1)

        tk.Label(popup, text="Descrição:").grid(row=1, column=0)
        descricao_entry = tk.Entry(popup)
        descricao_entry.grid(row=1, column=1)

        tk.Label(popup, text="Biblioteca:").grid(row=2, column=0)
        biblioteca_combo = ttk.Combobox(popup)
        biblioteca_combo.grid(row=2, column=1)
        self.update_biblioteca_dict()  # Atualiza o dicionário de bibliotecas
        biblioteca_combo['values'] = list(self.biblioteca_dict.keys())

        tk.Button(popup, text="Cadastrar", command=submit).grid(row=3, column=0, columnspan=2)

    def cadastrar_membro(self):
        def submit():
            nome = nome_entry.get()
            endereco = endereco_entry.get()
            biblioteca_nome = biblioteca_combo.get()
            biblioteca_id = self.biblioteca_dict.get(biblioteca_nome)
            if nome and endereco and biblioteca_id:
                membro = Membro(nome=nome, endereco=endereco, biblioteca_id=biblioteca_id)
                session.add(membro)
                session.commit()
                self.update_membro_dict()  # Atualiza o dicionário de membros
                messagebox.showinfo("Sucesso", "Membro cadastrado com sucesso!")
                popup.destroy()
            else:
                messagebox.showwarning("Atenção", "Por favor, preencha todos os campos.")

        popup = tk.Toplevel(self)
        popup.title("Cadastrar Membro")

        tk.Label(popup, text="Nome:").grid(row=0, column=0)
        nome_entry = tk.Entry(popup)
        nome_entry.grid(row=0, column=1)

        tk.Label(popup, text="Endereço:").grid(row=1, column=0)
        endereco_entry = tk.Entry(popup)
        endereco_entry.grid(row=1, column=1)

        tk.Label(popup, text="Biblioteca:").grid(row=2, column=0)
        biblioteca_combo = ttk.Combobox(popup)
        biblioteca_combo.grid(row=2, column=1)
        self.update_biblioteca_dict()  # Atualiza o dicionário de bibliotecas
        biblioteca_combo['values'] = list(self.biblioteca_dict.keys())

        tk.Button(popup, text="Cadastrar", command=submit).grid(row=3, column=0, columnspan=2)

    def listar_livros(self):
        def listar():
            biblioteca_nome = biblioteca_combo.get()
            biblioteca_id = self.biblioteca_dict.get(biblioteca_nome)
            biblioteca = session.query(Biblioteca).filter_by(id=biblioteca_id).first()
            if biblioteca:
                livros = session.query(Livro).filter_by(biblioteca_id=biblioteca_id).all()
                livros_list.delete(0, tk.END)
                for livro in livros:
                    if livro.emprestado == 1:
                       livros_list.insert(tk.END, f"{livro.id}: {livro.nome} Situação: Emprestado")
                    else:
                        livros_list.insert(tk.END, f"{livro.id}: {livro.nome} Situação: Disponível")
            else:
                messagebox.showwarning("Atenção", "Biblioteca não encontrada.")

        popup = tk.Toplevel(self)
        popup.title("Listar Livros por Biblioteca")

        tk.Label(popup, text="Biblioteca:").grid(row=0, column=0)
        biblioteca_combo = ttk.Combobox(popup)
        biblioteca_combo.grid(row=0, column=1)
        self.update_biblioteca_dict()  # Atualiza o dicionário de bibliotecas
        biblioteca_combo['values'] = list(self.biblioteca_dict.keys())

        tk.Button(popup, text="Listar", command=listar).grid(row=1, column=0, columnspan=2)

        livros_list = tk.Listbox(popup)
        livros_list.grid(row=2, column=0, columnspan=2)

    def gerar_emprestimo(self):
        def pesquisar_livros():
            termo = livro_pesquisa_entry.get().lower()
            livros = session.query(Livro).filter(Livro.nome.ilike(f"%{termo}%")).all()
            if livros:
                livro_combo['values'] = [l.nome for l in livros]
                self.livro_dict = {l.nome: l.id for l in livros}
            else:
                livro_combo['values'] = []
                messagebox.showinfo("Sem Resultados", "Nenhum livro encontrado com esse termo.")

        def pesquisar_membros():
            termo = membro_pesquisa_entry.get().lower()
            membros = session.query(Membro).filter(Membro.nome.ilike(f"%{termo}%")).all()
            if membros:
                membro_combo['values'] = [m.nome for m in membros]
                self.membro_dict = {m.nome: m.id for m in membros}
            else:
                membro_combo['values'] = []
                messagebox.showinfo("Sem Resultados", "Nenhum membro encontrado com esse termo.")

        def submit():
            livro_nome = livro_combo.get()
            membro_nome = membro_combo.get()
            livro_id = self.livro_dict.get(livro_nome)
            membro_id = self.membro_dict.get(membro_nome)
            livro = session.query(Livro).filter_by(id=livro_id).first()
            membro = session.query(Membro).filter_by(id=membro_id).first()
            if livro and membro:
                if not livro.emprestado:
                    livro.emprestado = True
                    livro.data_emprestimo = date.today()  # Defina a data atual aqui
                    livro.data_devolucao = data_devolucao.get()
                    membro.historico = (membro.historico + f", {livro.nome}" if membro.historico else livro.nome)
                    session.commit()
                    messagebox.showinfo("Sucesso", "Empréstimo realizado com sucesso!")
                    popup.destroy()
                else:
                    messagebox.showwarning("Atenção", "Livro já está emprestado.")
            else:
                messagebox.showwarning("Atenção", "Livro ou Membro não encontrado.")

        popup = tk.Toplevel(self)
        popup.title("Gerar Empréstimo de Livro")

        tk.Label(popup, text="Pesquisar Livro:").grid(row=0, column=0)
        livro_pesquisa_entry = tk.Entry(popup)
        livro_pesquisa_entry.grid(row=0, column=1)
        tk.Button(popup, text="Pesquisar", command=pesquisar_livros).grid(row=0, column=2)

        tk.Label(popup, text="Livro:").grid(row=1, column=0)
        livro_combo = ttk.Combobox(popup)
        livro_combo.grid(row=1, column=1)

        tk.Label(popup, text="Pesquisar Membro:").grid(row=2, column=0)
        membro_pesquisa_entry = tk.Entry(popup)
        membro_pesquisa_entry.grid(row=2, column=1)
        tk.Button(popup, text="Pesquisar", command=pesquisar_membros).grid(row=2, column=2)

        tk.Label(popup, text="Membro:").grid(row=3, column=0)
        membro_combo = ttk.Combobox(popup)
        membro_combo.grid(row=3, column=1)
        
        tk.Label(popup, text="Data de devolução:").grid(row=4, column=0)
        data_devolucao = DateEntry(popup)
        data_devolucao.grid(row=5, column=0)

        tk.Button(popup, text="Emprestar", command=submit).grid(row=7, column=1, columnspan=3)
        
    def devolver_livro(self):
        def pesquisar_livros():
            termo = livro_pesquisa_entry.get().lower()
            livros = session.query(Livro).filter(Livro.nome.ilike(f"%{termo}%")).all()
            if livros:
                livro_combo['values'] = [l.nome for l in livros]
                self.livro_dict = {l.nome: l.id for l in livros}
            else:
                livro_combo['values'] = []
                messagebox.showinfo("Sem Resultados", "Nenhum livro encontrado com esse termo.")
    
        def pesquisar_membros():
            termo = membro_pesquisa_entry.get().lower()
            membros = session.query(Membro).filter(Membro.nome.ilike(f"%{termo}%")).all()
            if membros:
                membro_combo['values'] = [m.nome for m in membros]
                self.membro_dict = {m.nome: m.id for m in membros}
            else:
                membro_combo['values'] = []
                messagebox.showinfo("Sem Resultados", "Nenhum membro encontrado com esse termo.")
    
        def submit():
            livro_nome = livro_combo.get()
            membro_nome = membro_combo.get()
            livro_id = self.livro_dict.get(livro_nome)
            membro_id = self.membro_dict.get(membro_nome)
            livro = session.query(Livro).filter_by(id=livro_id).first()
            membro = session.query(Membro).filter_by(id=membro_id).first()
            if livro and membro:
                if livro.emprestado:
                    livro.emprestado = False
                    livro.data_emprestimo = None
                    livro.data_devolucao = None
                    # Remove o livro do histórico do membro
                    membro.historico = ", ".join(l for l in membro.historico.split(", ") if l != livro.nome)
                    session.commit()
                    messagebox.showinfo("Sucesso", "Livro devolvido com sucesso!")
                    popup.destroy()
                else:
                    messagebox.showwarning("Atenção", "O livro não está emprestado.")
            else:
                messagebox.showwarning("Atenção", "Livro ou Membro não encontrado.")

        popup = tk.Toplevel(self)
        popup.title("Devolver Livro")
    
        tk.Label(popup, text="Pesquisar Livro:").grid(row=0, column=0)
        livro_pesquisa_entry = tk.Entry(popup)
        livro_pesquisa_entry.grid(row=0, column=1)
        tk.Button(popup, text="Pesquisar", command=pesquisar_livros).grid(row=0, column=2)
    
        tk.Label(popup, text="Livro:").grid(row=1, column=0)
        livro_combo = ttk.Combobox(popup)
        livro_combo.grid(row=1, column=1)
    
        tk.Label(popup, text="Pesquisar Membro:").grid(row=2, column=0)
        membro_pesquisa_entry = tk.Entry(popup)
        membro_pesquisa_entry.grid(row=2, column=1)
        tk.Button(popup, text="Pesquisar", command=pesquisar_membros).grid(row=2, column=2)
    
        tk.Label(popup, text="Membro:").grid(row=3, column=0)
        membro_combo = ttk.Combobox(popup)
        membro_combo.grid(row=3, column=1)
    
        tk.Button(popup, text="Devolver", command=submit).grid(row=4, column=0, columnspan=3)

    

    def listar_bibliotecas(self):
        popup = tk.Toplevel(self)
        popup.title("Listar Bibliotecas")

        bibliotecas_list = tk.Listbox(popup)
        bibliotecas_list.grid(row=0, column=0, columnspan=2)

        bibliotecas = session.query(Biblioteca).all()
        for biblioteca in bibliotecas:
            bibliotecas_list.insert(tk.END, f"{biblioteca.id}: {biblioteca.nome}, {biblioteca.endereco}")

if __name__ == "__main__":
    app = BibliotecaApp()
    app.mainloop()




