from scripts.token import *
import ply.lex as lex

t_ENTERO = r"([1-9][0-9]*|0)"
t_FLOTANTE = r"([1-9]\d*|0)+[.]\d+"
t_CHAR = r"[/]."
t_PAR_DER = r"[)]"
t_PAR_IZQ = r"[(]"
t_COR_DER = r"\["
t_COR_IZQ = r"\]"
t_SUMA = r'\+'
t_RESTA = r'\-'
t_EQUAL_OP = r'\='
t_PRODUCTO = r'\*'
t_STRING = r'\".*\"'
t_DIVISION = r'\/'
t_POTENCIA = r'\*\*'
t_AND = r'\&\&'
t_OR = r'\|\|'
t_NOT = r'\!'
t_EQUAL = r'\=\='
t_EQUAL_2 = r'\=\=\='
t_NOT_EQUAL = r'\!\='
t_MAYOR_QUE = r'\>'
t_MENOR_QUE = r'\<'

t_ignore = ' \t'
t_ignore_CM = r";.+"

def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("No es reconocido '%s'" % t.value[0])
    t.lexer.skip(1)

def t_NOMBRE(t):
    r"(_|[a-zA-Z])[a-zA-Z\d_]+"
    t.type = reservadas.get(t.value, 'NOMBRE')  # Check for reserved words
    return t
