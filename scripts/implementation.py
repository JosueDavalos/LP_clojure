from scripts.lexico import lexer
from scripts.sintactico import parser


def t_analizar_lexico(texto):
    lexer.input(texto)
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)


def t_analizar_sintaxis(texto):
    result = parser.parse(texto)
    print(result)
