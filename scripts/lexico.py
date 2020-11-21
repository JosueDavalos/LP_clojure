from scripts.tokens import *
import ply.lex as lex

t_ENTERO = r"([1-9][0-9]*|0)"
t_FLOTANTE = r"([1-9]\d*|0)+[.]\d+"
t_CHAR = r"[/]\S"
t_PAR_DER = r"[)]"
t_PAR_IZQ = r"[(]"
t_COR_DER = r"\["
t_COR_IZQ = r"\]"
t_COM_SIM = r"‘"
t_SUM = r'\+'
t_REST = r'\-'
t_EQUAL_OP = r'\='
t_PRODUCT = r'\*'
t_STRING = r'\"[^\"]*\"'
t_DIVISION = r'\/'
t_AND = r'and'
t_OR = r'or'
t_NOT = r'not'
t_EQUAL = r'\=\='
t_EQUAL_2 = r'\=\=\='
t_NOT_EQUAL = r'\!\='
t_GREATER_THAN = r'\>'
t_LESS_THAN = r'\<'
t_GREATER_THAN_EQUAL = r'\>\='
t_LESS_THAN_EQUAL = r'\<\='
t_ARGS = r"^\[(\w)*(\s\w+)*\]$"


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


# def t_METODONTH(t): luego mejorara con lexico de momento se declara solo la reservada nth
#     r"nth\s[a-z][a-zA-Z0-9]+\s\[([a-z][a-zA-Z0-9](\s[a-z][a-zA-Z0-9])*)*\]"
#     t.type = reservadas.get(t.value, 'METODONTH')  # Check for reserved words
#     return t

# def t_METODOFIRST(t):  luego mejorara con lexico de momento se declara solo la reservada first
#     r"first\s[a-z][a-zA-Z0-9]+\s?"
#     t.type = reservadas.get(t.value, 'METODOFIRST')  # Check for reserved words
#     return t

# def t_FUNCION(t):  luego mejorara con lexico de momento se declara solo la reservada defn
#     r"defn\s[a-z][a-zA-Z0-9]+\s"
#     t.type = reservadas.get(t.value, 'FUNCION')  # Check for reserved words
#     return t



lexer = lex.lex()
