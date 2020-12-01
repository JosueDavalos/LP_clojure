from scripts.tokens import tokens
import ply.yacc as yacc


# definir al menos 2 métodos para datos estructurados
# creación de funciones



# def p_sentencia_compuesta(p):
#     '''sentencia_compuesta : algoritmo
#                             | algoritmo sentencia_compuesta
#     '''

# def p_algoritmo(p):
#     '''algoritmo : variable
#                  | expresion
#                  | imprimir
#                  | controlStructures
#                  | funcion
#                  | metodo_lista
#                  | metodo_conjunto
#                  | metodo_vector
#                  | metodo_mapas
#     '''


# def p_funcion(p):
#     'funcion : PAR_IZQ DEFN NOMBRE argumentos sentencia_compuesta PAR_DER'

# def p_argumentos(p):
#     'argumentos :  COR_IZQ argumento COR_DER'

# def p_argumento(p):
#     '''argumento :   NOMBRE
#                     | NOMBRE argumento'''


# ## Metodos para LISTAS
# # (first lst)
# def p_metodo_lista_first(p):
#     '''metodo_lista : PAR_IZQ FIRST NOMBRE PAR_DER
#                     | PAR_IZQ FIRST estructura_lista PAR_DER'''

# # (nth lst index)
# def p_metodo_lista_nth(p):
#     '''metodo_lista : PAR_IZQ NTH NOMBRE NOMBRE PAR_DER
#                     | PAR_IZQ NTH NOMBRE ENTERO PAR_DER
#                     | PAR_IZQ NTH estructura_lista ENTERO PAR_DER
#                     | PAR_IZQ NTH estructura_lista NOMBRE PAR_DER'''

# # (cons element lst)
# def p_metodo_lista_cons(p):
#     '''metodo_lista : PAR_IZQ CONS valor NOMBRE PAR_DER
#                     | PAR_IZQ CONS valor estructura_lista PAR_DER'''

# ## FIN Metodos para LISTAS


# ## Metodos para CONJUNTOS
# # (get setofelements index)
# def p_metodo_conjunto_get(p):
#     '''metodo_conjunto : PAR_IZQ GET estructura_conjunto NOMBRE PAR_DER
#                         | PAR_IZQ GET estructura_conjunto ENTERO PAR_DER
#     '''

# # (conj setofelements x)
# def p_metodo_conjunto_conj(p):
#     'metodo_conjunto : PAR_IZQ CONJ estructura_conjunto valor PAR_DER'
# ## FIN Metodos para CONJUNTOS


# ## Metodos para VECTORES
# # (get vec index)
# def p_metodo_vector_get(p):
#     '''metodo_vector : PAR_IZQ GET estructura_vector NOMBRE PAR_DER
#                         | PAR_IZQ GET estructura_vector ENTERO PAR_DER
#     '''

# # (conj vec x)
# def p_metodo_vector_conj(p):
#     'metodo_vector : PAR_IZQ CONJ estructura_vector valor PAR_DER'
# ## FIN Metodos para VECTORES


# ## Metodos para MAPAS
# # (get hmap key)
# def p_metodo_mapas_get(p):
#     '''metodo_mapas : PAR_IZQ GET estructura_mapa STRING PAR_DER
#                     | PAR_IZQ GET estructura_mapa NOMBRE PAR_DER
#                     | PAR_IZQ GET NOMBRE NOMBRE PAR_DER
#                     | PAR_IZQ GET NOMBRE STRING PAR_DER
#     '''

# # (keys hmap)
# def p_metodo_mapas_conj(p):
#     '''metodo_mapas : PAR_IZQ KEYS estructura_mapa PAR_DER
#                     | PAR_IZQ KEYS NOMBRE PAR_DER'''
# ## FIN Metodos para MAPAS


# def p_expresion(p):
#     '''expresion : valor
#                  | estructura
#                  | expresionAritmetica
#                  | comparation
#                  | comparationLogic
#     '''

# # Agrupo las estructuras para poder trabajar con los diferentes metodos para cada una
# def p_estructura(p):
#     '''estructura : estructura_mapa
#                     | estructura_lista
#                     | estructura_conjunto
#                     | estructura_vector'''





# # cambio nombre de expresion
# def p_estructura_lista(p):
#     '''estructura_lista : PAR_IZQ LISTA PAR_IZQ compuesto PAR_DER PAR_DER
#                   | COM_SIM PAR_IZQ compuesto PAR_DER
#                   | PAR_IZQ LISTA compuesto PAR_DER
#     '''

# # cambio nombre de expresion
# def p_estructura_conjunto(p):
#     '''estructura_conjunto : PAR_IZQ CONJUNTO COM_SIM PAR_IZQ compuesto PAR_DER PAR_DER
#                   | HASH LLAV_IZQ compuesto LLAV_DER
#     '''

# # cambio nombre de expresion
# def p_estructura_vector(p):
#     '''estructura_vector : PAR_IZQ VECTOR compuesto PAR_DER
#                   | COR_IZQ compuesto COR_DER
#     '''

# # cambio nombre de expresion
# def p_estructura_mapa(p):
#     '''estructura_mapa : LLAV_IZQ parclaves LLAV_DER
#                   | PAR_IZQ mapas parclaves PAR_DER
#     '''