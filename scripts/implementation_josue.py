from scripts.token import *
import ply.lex as lex

# definir operaciones matematicas y condiciones de acuerdo a los tipos de datos mencionados
#metodos de impresion, lectura de datos
#definir 3 estructuras de control basicas

t_SUM = r'\+'
t_REST = r'\-'
t_EQUAL_OP = r'\='
t_PRODUCT = r'\*'
t_STRING = r'\"[^\"]*\"'
t_DIVISION = r'\/'
t_POW = r'\*\*'
t_AND = r'\&\&'
t_OR = r'\|\|'
t_NOT = r'(\!|not)'
t_EQUAL = r'\=\='
t_EQUAL_2 = r'\=\=\='
t_NOT_EQUAL = r'\!\='
t_GREATER_THAN = r'\>'
t_LESS_THAN = r'\<'
t_GREATER_THAN_EQUAL = r'\>\='
t_LESS_THAN_EQUAL = r'\<\='
