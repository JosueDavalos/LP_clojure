from scripts.tokens import tokens
import ply.yacc as yacc

#estructura de variables e inicializacion
#tipos de datos: enteros flotantes booleanos
#datos estructurados: str, listas, vector, mapas, set

def p_algoritmo(p):
    '''algoritmo : variable
                 | expresion
    '''

def p_variable(p):
    'variable : PAR_IZQ DEF NOMBRE expresion PAR_DER'

def p_expresion(p):
    '''expresion : valor
                 | estructura
                 | cadena'''

def p_estructura_lista(p):
    '''estructura : PAR_IZQ LISTA PAR_IZQ valor PAR_DER PAR_DER
                  | COM_SIM PAR_IZQ valor PAR_DER
    '''

def p_estructura_conjunto(p):
    '''estructura : PAR_IZQ CONJUNTO COM_SIM PAR_IZQ valor PAR_DER PAR_DER
                  | HASH LLAV_IZQ valor LLAV_DER
    '''

def p_estructura_vector(p):
    '''estructura : PAR_IZQ VECTOR valor PAR_DER
                  | COR_IZQ valor COR_DER
    '''

def p_estructura_mapa(p):
    '''estructura : LLAV_IZQ STRING STRING LLAV_DER
                  | PAR_IZQ mapas STRING STRING PAR_DER
    '''

def p_mapas(p):
    '''mapas : SORTEDMAP
             | HASHMAP
    '''

def p_valor(p):
    '''valor : numero
             | NOMBRE
             | booleano
    '''

def p_cadena(p):
    '''cadena : STRING
              | PAR_IZQ STR STRING PAR_DER
    '''

def p_booleano(p):
    '''booleano : TRUE
                | FALSE
    '''

def p_numero(p):
    '''numero : ENTERO
              | FLOTANTE
    '''

def p_error(p):
    print("Syntax error in input!")