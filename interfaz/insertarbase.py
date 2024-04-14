import tkinter as tk
from tkinter import ttk
import acciones

class InsertarBase(tk.Frame):
    def __init__(self):
        root = tk.Toplevel()
        super().__init__(root)
        root.geometry('500x600') 
        root.title('Insertar entrada')
        root.resizable(width=False, height=False)
        self.master = root
        self.config(bg='#f0f0f0') 
        self.pack(fill='both', expand=True)

        self.lbl_base = tk.Label(self, text="Insertar una entrada",
                                 bg='#f0f0f0', fg='#333', font=("Helvetica", 24))
        self.lbl_base.pack(side="top", pady=(20, 10))

 
        style = ttk.Style()
        style.configure("Treeview", background="#D3D3D3", foreground="black",
                        rowheight=25, fieldbackground="#D3D3D3")
        style.map("Treeview", background=[('selected', '#E58E26')])

        self.entradas = ttk.Treeview(self, style="Treeview")
        self.entradas.pack(side="top", fill='both', expand=True, padx=10, pady=10)
        self.entradas.tag_bind("tag_select", "<<TreeviewSelect>>", self.item_selected)
        self.fill_base_tree_view()

    
        self.input_frame = tk.Frame(self, bg='#f0f0f0')
        self.input_frame.pack(fill='x', padx=10, pady=10)

        self.lbl_entry = tk.Label(self.input_frame, text="Nombre de la entrada:",
                                  bg='#f0f0f0', fg='#333', font=("Helvetica", 12))
        self.lbl_entry.grid(row=0, column=0, sticky='w')
        self.txt_entry = tk.Entry(self.input_frame, width=50)
        self.txt_entry.grid(row=0, column=1, padx=5, pady=5)

        self.lbl_prop = tk.Label(self.input_frame, text="Propiedad:",
                                 bg='#f0f0f0', fg='#333', font=("Helvetica", 12))
        self.lbl_prop.grid(row=1, column=0, sticky='w')
        self.txt_prop = tk.Entry(self.input_frame, width=50)
        self.txt_prop.grid(row=1, column=1, padx=5, pady=5)

        self.btn_insertar = tk.Button(self.input_frame, text="Insertar",
                                      width=20, bg='#4CAF50', fg='white',
                                      command=self.add_propiedad)
        self.btn_insertar.grid(row=2, columnspan=2, pady=10)

        self.quit = tk.Button(self, text="Salir", width=20, fg='white',
                              bg='#F44336', command=self.master.destroy)
        self.quit.pack(side="bottom", pady=(5, 20))

    def fill_base_tree_view(self):
        self.entradas.delete(*self.entradas.get_children())
        base = self.entradas.insert("", tk.END, text="Base")
        base_entries = acciones.get_base_entries()
        for entry in base_entries:
            nombre = self.entradas.insert(base, tk.END, text=entry.name, tags=("tag_select",))
            for prop in entry.properties:
                self.entradas.insert(nombre, tk.END, text=prop.name)

    def add_propiedad(self):
        entrada = self.txt_entry.get()
        propiedad = self.txt_prop.get()
        acciones.insertar(entrada, propiedad)
        self.txt_entry.delete(0, tk.END)  
        self.txt_prop.delete(0, tk.END)
        self.fill_base_tree_view()

    def item_selected(self, event):
        id = event.widget.focus()
        text = self.entradas.item(id)["text"]
        self.txt_entry.delete(0, tk.END)
        self.txt_entry.insert(0, text)