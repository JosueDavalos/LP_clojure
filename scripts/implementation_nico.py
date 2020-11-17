from scripts.token import *
import ply.lex as lex




t_ENTERO = r"([1-9][0-9]*|0)"
t_FLOTANTE = r"([1-9]\d*|0)+[.]\d+"
t_BOOLEANO = r"(true|false)"
t_CHAR = r"[/]."
t_PAR_DER = r"[)]"
t_PAR_IZQ = r"[(]"
t_COR_DER = r"\["
t_COR_IZQ = r"\]"





# t_ENTERO = r"([1-9][0-9]*|0)"
# t_FLOTANTE = r"([1-9]\d*|0)+[.]\d+"
# t_BOOLEANO = r"(true|false)"
# t_CHAR = r"[/]."
# t_STRING = r"[\"].+[\"]"
# t_CDER = r"[)]"
# t_CIZQ = r"[(]"
#t_LISTA = r""
#t_CONJUNTO = r""
#t_MAPA = r""
#t_VECTOR = r""

t_ignore = ' \t'
t_ignore_CM = r";.+"

def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("No es reconocido '%s'" % t.value[0])
    t.lexer.skip(1)

def t_NOMBRE(t):
    r"(_|[a-zA-Z])[a-zA-Z\d_]*"
    t.type = reservadas.get(t.value, 'NOMBRE')  # Check for reserved words
    return t

# lexer = lex.lex()

# def t_analizar(texto):
#     lexer.input(texto)
#     while True:
#         tok = lexer.token()
#         if not tok:
#             break  # No more input
#         print(tok)

# cont=True

# while cont:
#     data = input(">> ")
#     if data!="salir":
#         t_analizar(data)
#     else:
#         cont= False
