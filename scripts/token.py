reservadas={
    "def": "DEF",
    "nil": "NULL",
    "hash-map": "HASHMAP",
    "sorted-map": "SORTEDMAP",
    "vector": "VECTOR",
    "set": "SET",
    "str": "STR",
    'loop':'LOOP',
    'do':'DO',
    'when':'WHEN',
    'println':'PRINTLN',
    'recur': 'RECUR',
    'defn': 'DEFN',
    'first': 'METODOFIRST',
    "list": "LIST",
    "nth" : "METODONTH"
}

tokens = [
    "ENTERO",
    "FLOTANTE",
    "BOOLEANO",
    "CHAR",
    "STRING",
    "LISTA",
    "CONJUNTO",
    "MAPA",
    "FUNCION",
    "VARIABLE",
    "PAR_DER",
    "PAR_IZQ",
    "COR_DER",
    "COR_IZQ",
    "SUMA",
    "RESTA",
    "PRODUCTO",
    "DIVISION",
    "POTENCIA",
    'AND',
    "OR",
    "NOT",
    'EQUAL_OP',
    "EQUAL",
    "EQUAL_2",
    "NOT_EQUAL",
    "MAYOR_QUE",
    "MENOR_QUE",
    "ARGS"
]+ list(reservadas.values())