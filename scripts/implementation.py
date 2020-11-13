from scripts.implementation_josue import *
from scripts.implementation_nico import *
from scripts.implementation_sebas import *


lexer = lex.lex()

def t_analizar(texto):
    lexer.input(texto)
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)