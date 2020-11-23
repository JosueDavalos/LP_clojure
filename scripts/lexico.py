from scripts.tokens import *
import ply.lex as lex

t_ENTERO = r"([1-9][0-9]*|0)"
t_FLOTANTE = r"([1-9]\d*|0)+[.]\d+"
t_CHAR = r"[/]\S"
t_PAR_DER = r"[)]"
t_PAR_IZQ = r"[(]"
t_COR_DER = r"\]"
t_COR_IZQ = r"\["
t_COM_SIM = r"'"
t_SUM = r'\+'
t_REST = r'\-'
t_PRODUCT = r'\*'
t_STRING = r'\"[^\"]*\"'
t_DIVISION = r'\/'
t_EQUAL = r'\='
t_NOT_EQUAL = r'not\='
t_GREATER_THAN = r'\>'
t_LESS_THAN = r'\<'
t_GREATER_THAN_EQUAL = r'\>\='
t_LESS_THAN_EQUAL = r'\<\='
t_HASH = r'\#'
t_LLAV_IZQ = r'{' 
t_LLAV_DER = r'}'

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


lexer = lex.lex()
