from scripts.token import *
import ply.lex as lex

# definir al menos 2 métodos para datos estructurados
# creación de funciones


t_ARGS = r"^\[(\w)*(\s\w+)*\]$"

# def t_METODOLIST(t):
#     r"list\*\s[a-z][a-zA-Z0-9]+\s\[([a-z][a-zA-Z0-9](\s[a-z][a-zA-Z0-9])*)*\]"
#     t.type = reservadas.get(t.value, 'METODOLIST')  # Check for reserved words
#     return t
#
# def t_METODOFIRST(t):
#     r"first\s[a-z][a-zA-Z0-9]+\s?"
#     t.type = reservadas.get(t.value, 'METODOFIRST')  # Check for reserved words
#     return t

def t_FUNCION(t):
    r"defn\s[a-z][a-zA-Z0-9]+\s"
    t.type = reservadas.get(t.value, 'FUNCION')  # Check for reserved words
    return t