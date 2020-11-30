from scripts.lexico import lexer
from scripts.sintactico import parser


def t_analizar_lexico(texto):
    lexer.input(texto)
    toks = []
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        toks.append(tok)
    return toks


def t_analizar_sintaxis(texto):
    result = parser.parse(texto)
    return result

def check_code_clojure(texto):
    tokens = t_analizar_lexico(texto)
    sintaxis = t_analizar_sintaxis(texto)
    title = '-'*5 + texto + '-'*5
    result = title + '\n'
    for tok in tokens:
        result += str(tok) + '\n'

    result +=  'Sintásis...' + ( 'WRONG' if sintaxis else 'OK' )

    print(result)
    return result