import tkinter as tk
from tkinter import ttk
from scripts.implementation import t_analizar_sintaxis, t_analizar_lexico


class Window:
    def __init__(self, root):
        root.configure(background='#ECECEC')
        #Wightes
        self.welcome_lb = tk.Label(root, text='Analizador Clojure')
        self.code = tk.Text(root, height=25, width=60)
        self.lexico_btn = tk.Button(root, text='Revisar Léxico', command=self.check_code_lexico, bg = "#0A0A2A", fg = "white")
        self.sintaxis_btn = tk.Button(root, text='Revisar Sintáctico', command=self.check_code_sintactico, bg = "#0A0A2A", fg = "white")
        self.results = tk.Label(root, text='Resultados de los analísis')
        self.results.config(width=50, height=26)


        #Propertiers of the windows
        root.title('Clojure ❤')
        root.geometry('900x500')
        self.welcome_lb.config(font=("Arial", 15))

        #position Wightes
        self.welcome_lb.grid(sticky = tk.E, pady = 5)
        self.code.grid()
        self.sintaxis_btn.grid(column=0, row=2,  sticky = tk.E)
        self.lexico_btn.grid(column=0, row=2,  sticky = tk.W, pady = 20)
        self.results.grid(column=1, row=1)


        #icon
        icon = tk.PhotoImage(file = "scripts/Clojure_logo.png")
        root.iconphoto(False, icon)      


    def check_code_lexico(self):
        text_code = self.code.get('1.0', 'end-1c')
        ## line by line
        # result = ''
        # for text in text_code.split('\n'):
        #     tokens = t_analizar_lexico(text)
        #     for tok in tokens:
        #         result += str(tok) + '\n'
        #     result += '\n'

        result = ''
        tokens = t_analizar_lexico(text_code)
        for tok in tokens:
            result += str(tok) + '\n'
        self.results.configure(text=result, justify='left')


    def check_code_sintactico(self):
        text_code = self.code.get('1.0', 'end-1c')
        ##line by line
        # result = ''
        # for text in text_code.split('\n'):
        #     if len(text) != 0: 
        #         sintaxis = t_analizar_sintaxis(text)
        #         result +=  '%s ...... '%text + ( 'WRONG' if sintaxis else 'OK' ) + '\n'

        sintaxis = t_analizar_sintaxis(text_code)
        result =  'Sintáctico ...... ' + ( 'WRONG' if sintaxis else 'OK' ) + '\n'
        self.results.configure(text=result, justify='left')





# app = tk.Tk()
# window = Window(app)
# app.mainloop()
