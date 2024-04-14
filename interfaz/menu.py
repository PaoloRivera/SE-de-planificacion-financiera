import tkinter as tk
from tkinter import PhotoImage
import interfaz.insertarbase as insertar_base
import interfaz.consultarbase as consultar_base

class Interfaz(tk.Frame):
    def __init__(self):
        root = tk.Tk()
        super().__init__(root)
        root.geometry('800x600')
        root.title('SE para Planificación Financiera')
        root.resizable(width=False, height=False)
        self.master = root
        self.config(bg='#f0f0f0')
        self.pack(fill='both', expand=True)

        self.lbl_base = tk.Label(self, text="Sistema Experto para Planificación Financiera",
                                 bg='#f0f0f0', fg='#333', font=("Helvetica", 24, "bold"))
        self.lbl_base.pack(side="top", pady=(20, 10))

        self.logo = PhotoImage(file="logo.png").subsample(4, 4) 
        self.logo_label = tk.Label(self, image=self.logo, bg='#f0f0f0')
        self.logo_label.pack(side="top", pady=(0, 20))

        self.buttons_frame = tk.Frame(self, bg='#f0f0f0')
        self.buttons_frame.pack(fill='x', pady=20)

        self.txt_insertar = tk.Button(self.buttons_frame, text="Insertar a base de conocimiento",
                                      width=30, height=2, bg='#4CAF50', fg='white',
                                      command=insertar_base.InsertarBase)
        self.txt_insertar.pack(side="top", padx=5, pady=5)

        self.txt_consultar = tk.Button(self.buttons_frame, text="Consultar",
                                       width=30, height=2, bg='#2196F3', fg='white',
                                       command=consultar_base.ConsultarBase)
        self.txt_consultar.pack(side="top", padx=5, pady=5)

        self.quit = tk.Button(self.buttons_frame, text="Salir", width=30, height=2,
                              bg='#F44336', fg='white', command=self.master.destroy)
        self.quit.pack(side="top", padx=5, pady=(5, 20))
