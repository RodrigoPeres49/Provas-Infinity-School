from customtkinter import CTk
import customtkinter as ctk

root = CTk()

class Tela:
    
    # CONSTRUTOR DA TELA
    
    def __init__(self, root):
        self.root = root
        
        # CONFIGURAÇÕES DA JANELA 
        
        self.root.geometry("600x480")
        self.root.resizable(False, False)
        self.frames()
        self.widgets()
        self.root.grid_propagate(False)
                
        # CENTRALIZAR ELEMENTOS PELO GRID
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(2, weight=1)
    
    # FRAME DENTRO DA JANELA
    
    def frames(self):   
        self.frame = ctk.CTkFrame(self.root, fg_color="lightgreen", width=500, height=400)
        self.frame.grid(column=1, row=1) 
        self.frame.grid_propagate(False)
        
        # CENTRALIZAR ELEMENTOS NO FRAME
        
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(3, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(6, weight=1)
    
    # WIDGETS
         
    def widgets(self):
        
        titulo = ctk.CTkLabel(self.frame, text="CONVERSOR DE MEDIDAS", font= ('Verdana', 20, 'bold'))
        titulo.grid(column=1, row=1, columnspan= 2, padx=20, pady=20)
        seletor_label = ctk.CTkLabel(self.frame, text="Selecione uma medida para conversão:")
        seletor_label.grid(column=1, row=2, columnspan=2, padx=5, pady=5)
        
        
        # UTILIZANDO O METODO COMBOBOX PARA SELECIONAR A MEDIDA
        
        self.seletor1 = ctk.CTkComboBox(self.frame, values=["Milímetros", "Centímetros", "Metros", "Kilometros"], state='readonly')
        self.seletor1.grid(column=1, row=3, padx=5, pady=5)
        
        # VALORES DENTRO DA COMBOBOX E O VALOR INICIAL DA PRIMEIRA É CENTIMETROS
        
        self.seletor1.set("Centímetros")
        
        self.seletor1_entry = ctk.CTkEntry(self.frame)
        self.seletor1_entry.grid(column=2, row=3, padx=5, pady=5)
        
        self.seletor2 = ctk.CTkComboBox(self.frame, values=["Milímetros", "Centímetros", "Metros", "Kilometros"], state='readonly')
        self.seletor2.grid(column=1, row=4, padx=5, pady=5)
        
        # VALOR INICIAL DO SEGUNDO CAMPO É METROS
        
        self.seletor2.set("Metros")
        
        # O SEGUNDO CAMPO DO ENTRY É AONDE SERÁ EXIBIDO O VALOR CONVERTIDO, NÃO PODERÁ SER EDITADO 
        
        self.seletor2_entry = ctk.CTkEntry(self.frame, state='readonly')
        self.seletor2_entry.grid(column=2, row=4, padx=5, pady=5)
        
        # BOTÃO PARA CHAMAR A FUNÇÃO DE CONVERSÃO ABAIXO
        
        self.conversor = ctk.CTkButton(self.frame, text="Converter", command=self.converter_medidas)
        self.conversor.grid(row=5, column=1, columnspan=2, padx=10, pady=10)
    
    
    # FUNCÃO PARA CONVERTER MEDIDAS  
        
    def converter_medidas(self):
        self.seletor1_var = self.seletor1.get()
        self.var_1 = self.seletor1_entry.get()
        self.seletor2_var = self.seletor2.get()
        
        # SE O VALOR FOR VAZIO OU 0 ELE RETORNA COMO 0 OS DOIS CAMPOS
            
        if self.var_1 == "" or self.var_1 is None:
            
            # DEVE-SE EDITAR O ESTADO DO DA VARIÁVEL " self.seleto2_entry " PARA NORMAL E INSERIR O VALOR CONVERTIDO
            # DEPOIS VOLTAR PARA O ESTADO DE SOMENTE LEITURA = " state= "readonly" "
            
            self.seletor1_entry.insert(0,'0')
            self.seletor2_entry.configure(state='normal')
            self.seletor2_entry.delete(0, "end")
            self.seletor2_entry.insert(0,'0.0')  
            self.seletor2_entry.configure(state='readonly')
        
        
        else:
            
            self.var_1 = float(self.seletor1_entry.get())
            
            if self.seletor1_var == "Milímetros":
                if self.seletor2_var == "Centímetros":
                    self.var_2 = self.var_1 / 10
                elif self.seletor2_var == "Metros":
                    self.var_2 = self.var_1 / 1000
                elif self.seletor2_var == "Kilometros":
                    self.var_2 = self.var_1 / 1000000
                else:
                    self.var_2 = self.var_1

            elif self.seletor1_var == "Centímetros":
                if self.seletor2_var == "Milímetros":
                    self.var_2 = self.var_1 * 10
                elif self.seletor2_var == "Metros":
                    self.var_2 = self.var_1 / 100
                elif self.seletor2_var == "Kilometros":
                    self.var_2 = self.var_1 / 100000
                else:
                    self.var_2 = self.var_1

            elif self.seletor1_var == "Metros":
                if self.seletor2_var == "Milímetros":
                    self.var_2 = self.var_1 * 1000
                elif self.seletor2_var == "Centímetros":
                    self.var_2 = self.var_1 * 100
                elif self.seletor2_var == "Kilometros":
                    self.var_2 = self.var_1 / 1000
                else:
                    self.var_2 = self.var_1

            elif self.seletor1_var == "Kilometros":
                if self.seletor2_var == "Milímetros":
                    self.var_2 = self.var_1 * 1000000
                elif self.seletor2_var == "Centímetros":
                    self.var_2 = self.var_1 * 100000
                elif self.seletor2_var == "Metros":
                    self.var_2 = self.var_1 * 1000
                else:
                    self.var_2 = self.var_1
    
        
            # DEVE-SE EDITAR O ESTADO DO DA VARIÁVEL " self.seleto2_entry " PARA NORMAL E INSERIR O VALOR CONVERTIDO
            # DEPOIS VOLTAR PARA O ESTADO DE SOMENTE LEITURA = " state= "readonly" "
        
            self.seletor2_entry.configure(state='normal')
            self.seletor2_entry.delete(0, "end")
            self.seletor2_entry.insert(0, str(self.var_2))  
            self.seletor2_entry.configure(state='readonly')    

# EXECUTAR JANELA                 

if __name__ == '__main__':
    app = Tela(root)
    root.mainloop()

    

