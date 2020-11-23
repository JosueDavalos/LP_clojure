from scripts.tokens import tokens
from scripts.implementation_josue import *
import ply.yacc as yacc



#estructura de variables e inicializacion
#tipos de datos: enteros flotantes booleanos
#datos estructurados: str, listas, vector, mapas, set

def p_algoritmo(p):
    '''algoritmo : variable
                 | expresion
                 | imprimir
                 | controlStructures
    '''

def p_variable(p):
    'variable : PAR_IZQ DEF NOMBRE expresion PAR_DER'

def p_expresion(p):
    '''expresion : valor
                 | estructura
                 | expresionAritmetica
                 | comparation
                 | comparationLogic
    '''

### Josue
def p_control_structures(p):
    ''' controlStructures : if
                          | while
                          | loop
    '''

def p_loop_statement(p):
    '''loop : PAR_IZQ LOOP COR_IZQ compuesto COR_DER when PAR_DER
    '''

def p_when_loop_statement(p):
    '''when : PAR_IZQ WHEN comparation algoritmo recur PAR_DER
    '''

def p_recur_loop_statement(p):
    '''recur : PAR_IZQ RECUR expresionAritmetica PAR_DER
    '''

def p_while_statement(p):
    '''while : PAR_IZQ WHILE comparation PAR_IZQ DO algoritmo PAR_DER
    '''

def p_if_statement(p):
    '''if : PAR_IZQ IF booleanExpresion expresion expresion PAR_DER
          | PAR_IZQ IF booleanExpresion expresion PAR_DER
    '''

def p_boolean_expresion(p):
    '''booleanExpresion : FALSE
                        | TRUE
                        | comparationLogic
                        | comparation
    '''

def p_imprimir(p):
    '''imprimir : PAR_IZQ imprimirOptions expresion PAR_DER
    '''

def p_comparation_logic(p):
    '''comparationLogic :  PAR_IZQ operadorLogic valor valor PAR_DER 
                      | PAR_IZQ NOT valor PAR_DER
    '''

def p_comparation(p):
    'comparation : PAR_IZQ operadorCompare valor valor PAR_DER'


def p_expresion_aritmetic(p):
    '''expresionAritmetica : PAR_IZQ operadorMath numberSerie PAR_DER
    '''

def p_number_serie(p):
    '''numberSerie : numero
                    | NOMBRE
                    | expresionAritmetica
                    | numero numberSerie
                    | NOMBRE numberSerie
                    | expresionAritmetica numberSerie
    '''
### End Josue



# cambie valor por compuesto aqui
def p_estructura_lista(p):
    '''estructura : PAR_IZQ LISTA PAR_IZQ compuesto PAR_DER PAR_DER
                  | COM_SIM PAR_IZQ compuesto PAR_DER
    '''
# cambie valor por compuesto aqui
def p_estructura_conjunto(p):
    '''estructura : PAR_IZQ CONJUNTO COM_SIM PAR_IZQ compuesto PAR_DER PAR_DER
                  | HASH LLAV_IZQ compuesto LLAV_DER
    '''

# cambie valor por compuesto aqui
def p_estructura_vector(p):
    '''estructura : PAR_IZQ VECTOR compuesto PAR_DER
                  | COR_IZQ compuesto COR_DER
    '''

def p_estructura_mapa(p):
    '''estructura : LLAV_IZQ parclaves LLAV_DER
                  | PAR_IZQ mapas parclaves PAR_DER
    '''

def p_mapas(p):
    '''mapas : SORTEDMAP REST MAP
             | HASHMAP REST MAP
    '''

def p_compuesto(p):
    '''compuesto : valor
                 | valor compuesto
    '''
def p_parclaves(p):
    '''parclaves : STRING STRING
                 | STRING STRING parclaves
    '''

def p_valor(p):
    '''valor : numero
             | NOMBRE
             | booleano
             | cadena
    '''

def p_cadena(p):
    '''cadena : STRING
              | PAR_IZQ STR STRING STRING PAR_DER
    '''

def p_booleano(p):
    '''booleano : TRUE
                | FALSE
    '''

def p_numero(p):
    '''numero : ENTERO
              | FLOTANTE
    '''



### Josue
def p_operador_math(p):
    '''operadorMath : SUM 
                    | REST 
                    | PRODUCT 
                    | DIVISION
    '''


def p_operador_comparation(p):
    '''operadorCompare : EQUAL
                        | NOT_EQUAL
                        | GREATER_THAN
                        | LESS_THAN
                        | GREATER_THAN_EQUAL
                        | LESS_THAN_EQUAL
    '''

def p_operador_logic(p):
    '''operadorLogic : AND
                     | OR
    '''

def p_imprimir_options(p):
    '''imprimirOptions : PRINT
                        | PRINTLN
    '''
### end Josue



def p_error(p):
    print("Syntax error in input!")



parser = yacc.yacc() 