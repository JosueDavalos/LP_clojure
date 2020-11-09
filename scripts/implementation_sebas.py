import ply.lex as lex

reservadas={
    "def": "DEF",
    "nil": "NULL",
    "hash-map": "HASHMAP",
    "sorted-map": "SORTEDMAP",
    "list": "LIST",
    "vector": "PVECTOR",
    "set": "SET",
    "str": "STR"
}

tokens = [
    "LISTA",
    "CONJUNTO",
    "MAPA",
    "VECTOR",
    "VARIABLE",
    "FUNCION"
]+ list(reservadas.values())

#t_ENTERO = r"([1-9][0-9]*|0)"
#t_FLOTANTE = r"([1-9]\d*|0)+[.]\d+"
#t_BOOLEANO = r"(true|false)"
#t_CHAR = r"[/]."
#t_STRING = r"[\"].+[\"]"
#t_CDER = r"[)]"
#t_CIZQ = r"[(]"
t_LISTA = r"^\(list\s((\s?((\"\w+\")|(\'[a-z])))+|(\s?[0-9]+)+)\)$"
t_CONJUNTO = r""
t_MAPA = r""
t_VECTOR = r""
t_FUNCTION = r"^\(defn\s\w+\s\[(\w)*(\s\w+)*\]\s?((\(.+\))|(\s\(.+\))*)\)$"

t_ignore = ' \t'
t_ignore_CM = r";.+"