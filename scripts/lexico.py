import ply.lex as lex


reservadas={
    "def": "DEF",
    "hash": "HASHMAP",
    "sorted": "SORTEDMAP",
    "map": "MAP",
    "vector": "VECTOR",
    "set": "CONJUNTO",
    "str": "STR",
    'loop':'LOOP',
    'while':'WHILE',
    'do':'DO',
    'when':'WHEN',
    'println':'PRINTLN',
    'print':'PRINT',
    'recur': 'RECUR',
    'defn': 'DEFN',
    'first': 'FIRST',
    "list": "LISTA",
    "nth" : "NTH",
    "if":"IF",
    "true": "TRUE",
    "false": "FALSE",
    'read':"READ",
    'line':"LINE",
    "not":"NOT",
    'and':'AND',
    'or':"OR",
    'cons':"CONS",
    'get':"GET",
    'conj':"CONJ",
    'keys':"KEYS"
}

tokens = list(reservadas.values())+[
    "ENTERO",
    "FLOTANTE",
    "STRING",
    "PAR_DER",
    "PAR_IZQ",
    "COR_DER",
    "COR_IZQ",
    "SUM",
    "REST",
    "PRODUCT",
    "DIVISION",
    "EQUAL",
    "NOT_EQUAL",
    "GREATER_THAN",
    "LESS_THAN",
    "GREATER_THAN_EQUAL",
    "LESS_THAN_EQUAL",
    "COM_SIM",
    "NOMBRE",
    "HASH",
    "LLAV_IZQ",
    "LLAV_DER",
    "COMA",
    "COMMENT"
]



t_ENTERO = r"([1-9][0-9]*|0)"
t_FLOTANTE = r"([1-9]\d*|0)+[.]\d+"
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
t_COMA = r','
t_EQUAL = r'\='
t_NOT_EQUAL = r'not\='
t_GREATER_THAN = r'\>'
t_LESS_THAN = r'\<'
t_GREATER_THAN_EQUAL = r'\>\='
t_LESS_THAN_EQUAL = r'\<\='
t_HASH = r'\#'
t_LLAV_IZQ = r'{' 
t_LLAV_DER = r'}'
t_COMMENT = r";.+"

t_ignore = ' \t'


errors = {'lexico': [], 'sintactico':[]}

def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("No es reconocido '%s'" % t.value[0])
    errors['lexico'].append(t.value[0])
    t.lexer.skip(1)

def t_NOMBRE(t):
    r"(_|[a-zA-Z])[a-zA-Z\d_]*"
    t.type = reservadas.get(t.value, 'NOMBRE')  # Check for reserved words
    return t


lexer = lex.lex()
