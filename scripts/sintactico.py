from scripts.lexico import tokens, errors
import ply.yacc as yacc


def p_sentencia_compuesta(p):
    '''sentencia_compuesta : algoritmo
                           | algoritmo sentencia_compuesta
    '''

def p_algoritmo(p):
    '''algoritmo : variable
                 | expresion
                 | imprimir
                 | estructurasControl
                 | funcion
                 | metodo_lista
                 | metodo_conjunto
                 | metodo_vector
                 | metodo_mapas
    '''


def p_funcion(p):
    'funcion : PAR_IZQ DEFN NOMBRE argumentos sentencia_compuesta PAR_DER'

def p_argumentos(p):
    '''argumentos :  COR_IZQ argumento COR_DER
                  | COR_IZQ COR_DER
    '''

def p_argumento(p):
    '''argumento : NOMBRE
                 | NOMBRE argumento
    '''

# (first lst)
def p_metodo_lista_first(p):
    '''metodo_lista : PAR_IZQ FIRST NOMBRE PAR_DER
                    | PAR_IZQ FIRST estructura_lista PAR_DER'''

# (nth lst index)
def p_metodo_lista_nth(p):
    '''metodo_lista : PAR_IZQ NTH NOMBRE NOMBRE PAR_DER
                    | PAR_IZQ NTH NOMBRE ENTERO PAR_DER
                    | PAR_IZQ NTH estructura_lista ENTERO PAR_DER
                    | PAR_IZQ NTH estructura_lista NOMBRE PAR_DER'''

# (cons element lst)
def p_metodo_lista_cons(p):
    '''metodo_lista : PAR_IZQ CONS valor NOMBRE PAR_DER
                    | PAR_IZQ CONS valor estructura_lista PAR_DER'''


# (get setofelements index)
def p_metodo_conjunto_get(p):
    '''metodo_conjunto : PAR_IZQ GET estructura_conjunto NOMBRE PAR_DER
                       | PAR_IZQ GET estructura_conjunto ENTERO PAR_DER
    '''

# (conj setofelements x)
def p_metodo_conjunto_conj(p):
    'metodo_conjunto : PAR_IZQ CONJ estructura_conjunto valor PAR_DER'


# (get vec index)
def p_metodo_vector_get(p):
    '''metodo_vector : PAR_IZQ GET estructura_vector NOMBRE PAR_DER
                     | PAR_IZQ GET estructura_vector ENTERO PAR_DER
    '''

# (conj vec x)
def p_metodo_vector_conj(p):
    'metodo_vector : PAR_IZQ CONJ estructura_vector valor PAR_DER'


# (get hmap key)
def p_metodo_mapas_get(p):
    '''metodo_mapas : PAR_IZQ GET estructura_mapa STRING PAR_DER
                    | PAR_IZQ GET estructura_mapa NOMBRE PAR_DER
                    | PAR_IZQ GET NOMBRE NOMBRE PAR_DER
                    | PAR_IZQ GET NOMBRE STRING PAR_DER
    '''

# (keys hmap)
def p_metodo_mapas_conj(p):
    '''metodo_mapas : PAR_IZQ KEYS estructura_mapa PAR_DER
                    | PAR_IZQ KEYS NOMBRE PAR_DER'''


def p_variable(p):
    'variable : PAR_IZQ DEF NOMBRE expresion PAR_DER'


def p_expresion(p):
    '''expresion : valor
                 | estructura
                 | expresionAritmetica
                 | comparacion
                 | comparacionLogica
                 | input
    '''

def p_estructura(p):
    '''estructura : estructura_mapa
                  | estructura_lista
                  | estructura_conjunto
                  | estructura_vector'''



def p_control_estructuras(p):
    ''' estructurasControl : if
                           | while
                           | loop
    '''

def p_loop_sentencia(p):
    '''loop : PAR_IZQ LOOP COR_IZQ compuesto COR_DER when PAR_DER
    '''

def p_when_loop_sentencia(p):
    '''when : PAR_IZQ WHEN comparacion algoritmo recur PAR_DER
    '''

def p_recur_loop_sentencia(p):
    '''recur : PAR_IZQ RECUR expresionAritmetica PAR_DER
    '''

def p_while_sentencia(p):
    '''while : PAR_IZQ WHILE comparacion PAR_IZQ DO sentencia_compuesta PAR_DER PAR_DER
    '''

def p_if_sentencia(p):
    '''if : PAR_IZQ IF expresionBooleana sentencia_compuesta PAR_DER'''

def p_boolean_expresion(p):
    '''expresionBooleana : FALSE
                         | TRUE
                         | comparacionLogica
                         | comparacion
    '''

def p_input(p):
    'input : PAR_IZQ READ REST LINE PAR_DER'

def p_imprimir(p):
    '''imprimir : PAR_IZQ opcionesImprimir expresion PAR_DER
    '''

def p_comparacion_logica(p):
    '''comparacionLogica :  PAR_IZQ operadorLogico valor valor PAR_DER
                         | PAR_IZQ NOT valor PAR_DER
    '''

def p_comparacion(p):
    'comparacion : PAR_IZQ operadorComparacion valor valor PAR_DER'


def p_expresion_aritmetica(p):
    '''expresionAritmetica : PAR_IZQ operadorMat numberoSerie PAR_DER
    '''

def p_numbero_serie(p):
    '''numberoSerie : numero
                    | NOMBRE
                    | expresionAritmetica
                    | numero numberoSerie
                    | NOMBRE numberoSerie
                    | expresionAritmetica numberoSerie
    '''



def p_estructura_lista(p):
    '''estructura_lista : PAR_IZQ LISTA PAR_IZQ compuesto PAR_DER PAR_DER
                        | COM_SIM PAR_IZQ compuesto PAR_DER
                        | PAR_IZQ LISTA compuesto PAR_DER
    '''

def p_estructura_conjunto(p):
    '''estructura_conjunto : PAR_IZQ CONJUNTO COM_SIM PAR_IZQ compuesto PAR_DER PAR_DER
                           | HASH LLAV_IZQ compuesto LLAV_DER
    '''


def p_estructura_vector(p):
    '''estructura_vector : PAR_IZQ VECTOR compuesto PAR_DER
                         | COR_IZQ compuesto COR_DER
    '''


def p_estructura_mapa(p):
    '''estructura_mapa : LLAV_IZQ parclaves LLAV_DER
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
                 | STRING STRING COMA parclaves
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


def p_operador_mat(p):
    '''operadorMat : SUM
                   | REST
                   | PRODUCT
                   | DIVISION
    '''


def p_operador_comparacion(p):
    '''operadorComparacion : EQUAL
                           | NOT_EQUAL
                           | GREATER_THAN
                           | LESS_THAN
                           | GREATER_THAN_EQUAL
                           | LESS_THAN_EQUAL
    '''

def p_operador_logico(p):
    '''operadorLogico : AND
                      | OR
    '''

def p_imprimir_opciones(p):
    '''opcionesImprimir : PRINT
                        | PRINTLN
    '''

def p_error(p):
    print('sintaxis error')
    errors['sintactico'].append(p)
    # if p:
    #     print("Syntax error at token", p.type)
    #     parser.errok()
    # else:
    #     print(p)
    #     print("Syntax error at EOF")



parser = yacc.yacc() 