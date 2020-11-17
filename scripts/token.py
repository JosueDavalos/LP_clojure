reservadas={
    "def": "DEF",
    "nil": "NULL",
    "hash-map": "HASHMAP",
    "sorted-map": "SORTEDMAP",
    "vector": "VECTOR",
    "set": "CONJUNTO",
    "str": "STR",
    'loop':'LOOP',
    'do':'DO',
    'when':'WHEN',
    'println':'PRINTLN',
    'recur': 'RECUR',
    'defn': 'DEFN',
    'first': 'METODOFIRST',
    "list": "LISTA",
    "nth" : "METODONTH",
    "doseq": "DOSEQ", 
    "true": "TRUE",
    "false": "FALSE",
    "not":"NOT",
    "read-line": "READLINE"
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
    "POW",
    'AND',
    "OR",
    'EQUAL_OP',
    "EQUAL",
    "EQUAL_2",
    "NOT_EQUAL",
    "GREATER_THAN",
    "LESS_THAN",
    "ARGS",
    "COM_SIM",
    "NOMBRE"
]