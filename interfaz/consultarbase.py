import tkinter as tk
import tkinter.messagebox as messagebox
from experto_general.response import Response
from acciones import engine

class ConsultarBase(tk.Frame):
    def __init__(self):
        self.master = tk.Toplevel()
        super().__init__(self.master)

        self.master.geometry('400x200')  
        self.master.title('Consultar al sistema')
        self.master.resizable(width=False, height=False)
        self.config(bg='#f0f0f0')
        self.pack(fill='both', expand=True)

        self.lbl_question = tk.Label(self, text="PREGUNTA", bg='#f0f0f0',
                                     fg='#333', font=("Helvetica", 14))
        self.lbl_question.pack(side="top", pady=(40, 20))

        self.btn_frame = tk.Frame(self, bg='#f0f0f0')
        self.btn_frame.pack()

        self.btn_yes = tk.Button(self.btn_frame, text="Sí", width=15, bg='#4CAF50',
                                 fg='white', command=self._send_yes)
        self.btn_yes.pack(side="left", padx=10, pady=20)

        self.btn_no = tk.Button(self.btn_frame, text="No", width=15, bg='#F44336',
                                fg='white', command=self._send_no)
        self.btn_no.pack(side="right", padx=10, pady=20)

        self.questions = engine.generate()
        self._get_question(Response.NO)

    def _send_yes(self):
        self._get_question(Response.YES)

    def _send_no(self):
        self._get_question(Response.NO)

    def _get_question(self, response: Response):
        try:
            engine.set_response(response)
            question = next(self.questions)

            if question is not None:
                self.lbl_question.config(text=f"¿{question.name}?")
            else:
                self._finished()

        except StopIteration:
            self._finished()

    def _finished(self):
        if engine.result is None:
            messagebox.showerror("Error",
                                "No se encontró ninguna entrada que coincida con las propiedades ingresadas.")
        else:
            # Crea una nueva ventana para mostrar la recomendación
            recommendation_window = tk.Toplevel(self.master)
            recommendation_window.title("Recomendación")
            recommendation_window.geometry("500x600")
            recommendation_window.config(bg="#f0f0f0")
            
            header = tk.Label(recommendation_window, text="Recomendación del Sistema",
                            bg="#f0f0f0", fg="#333", font=("Helvetica", 16, "bold"))
            header.pack(pady=(10, 5))
            
            content_frame = tk.Frame(recommendation_window)
            content_frame.pack(fill="both", expand=True, padx=10, pady=5)
            
            text_area = tk.Text(content_frame, wrap="word", bg="white", font=("Helvetica", 12), bd=0, highlightthickness=0)
            text_area.pack(side="left", fill="both", expand=True)
            
            scrollbar = tk.Scrollbar(content_frame, command=text_area.yview)
            scrollbar.pack(side="right", fill="y")
            
            text_area.config(yscrollcommand=scrollbar.set)
            
            reason = f"Sugerido porque:\n\n"
            for prop in engine.result.properties:
                reason += f"- {prop.name}\n"
            recommendation_text = f"Se recomienda: {engine.result.name}\n\n{engine.result.description}\n\n{reason}"
            
            text_area.insert("1.0", recommendation_text)
            text_area.config(state="disabled")  # Hace el texto no editable

            close_button = tk.Button(recommendation_window, text="Cerrar", command=recommendation_window.destroy,
                                    bg="#F44336", fg="white", font=("Helvetica", 12), bd=0)
            close_button.pack(pady=(5, 10))

