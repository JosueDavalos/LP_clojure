import tkinter as tk
from tkinter import ttk
from scripts.lexico import errors
from scripts.implementation import t_analizar_sintaxis, t_analizar_lexico


class Window:
    def __init__(self, root):
        root.configure(background='#ECECEC')

        #Wightes
        self.code = tk.Text(root, height=25, width=60)
        self.lexico_btn = tk.Button(root, text='Análisis Léxico', command=self.check_code_lexico, bg = "#0A0A2A", fg = "white")
        self.sintaxis_btn = tk.Button(root, text='Análisis Sintáctico', command=self.check_code_sintactico, bg = "#0A0A2A", fg = "white")
        self.results = tk.Label(root, text='Resultados de los análisis')
        self.results.config(width=70, height=25)
        #self.frame = tk.Frame(root)
        #self.canvas = tk.Canvas(self.frame)
        #self.scroll = tk.Scrollbar(self.frame, orient="vertical", command=canvas.yview)
        #self.scroll.grid(row=0, column=1)
        #self.results = tk.Label(self.canvas, text='Resultados de los análisis')
        #self.results.config(width=70, height=25)
        #self.results.grid(column=0, row=1, padx=20)

        #Propertiers of the windows
        root.title('Analizador Clojure ❤')
        root.geometry('1055x550')

        #position Wightes
        self.code.grid(column=0, row=1,padx=20, pady=20)
        self.sintaxis_btn.grid(column=0, row=2,  sticky = tk.E, padx = 75, pady=10)
        self.lexico_btn.grid(column=1, row=2,  sticky = tk.W, padx = 75)
        self.results.grid(column=1, row=1, padx=20)

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

        there_are_error_lexico = len(errors['lexico'])!=0

        if there_are_error_lexico:
            result +=  'ERROR! Tokens no reconocidos: %s'% ', '.join(["'%s'"%x for x in errors['lexico']])

        errors['lexico'] = []
        errors['sintactico'] = []

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
        there_are_error_lexico = len(errors['lexico'])!=0
        there_are_error_sintactico =  len(errors['sintactico'])!=0
        there_are_errors = there_are_error_lexico or there_are_error_sintactico

        result =  'Sintáctico ...... ' + ( 'ERROR' if sintaxis or there_are_errors else 'OK' ) + '\n'

        if there_are_error_lexico:
            result +=  'ERROR! Tokens no reconocidos: %s'% ', '.join(["'%s'"%x for x in errors['lexico']])

        errors['lexico'] = []
        errors['sintactico'] = []
        self.results.configure(text=result, justify='left')





# app = tk.Tk()
# window = Window(app)
# app.mainloop()
