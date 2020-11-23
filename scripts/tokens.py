reservadas={
    "def": "DEF",
    "nil": "NULL",
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
    'first': 'METODOFIRST',
    "list": "LISTA",
    "nth" : "METODONTH",
    "if":"IF",
    "doseq": "DOSEQ", 
    "true": "TRUE",
    "false": "FALSE",
    "read-line": "READLINE",
    "not":"NOT",
    'and':'AND',
    'or':"OR"
}

tokens = list(reservadas.values())+[
    "ENTERO",
    "FLOTANTE",
    "CHAR",
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
    "LLAV_DER"
]
