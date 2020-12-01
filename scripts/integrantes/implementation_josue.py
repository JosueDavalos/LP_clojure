from scripts.tokens import tokens
import ply.yacc as yacc

# definir operaciones matematicas y condiciones de acuerdo a los tipos de datos mencionados
# metodos de impresion, lectura de datos
# definir 3 estructuras de control basicas


# def p_control_structures(p):
#     ''' controlStructures : if
#                           | while
#                           | loop
#     '''

# def p_loop_statement(p):
#     '''loop : PAR_IZQ LOOP COR_IZQ compuesto COR_DER when PAR_DER
#     '''

# def p_when_loop_statement(p):
#     '''when : PAR_IZQ WHEN comparation algoritmo recur PAR_DER
#     '''

# def p_recur_loop_statement(p):
#     '''recur : PAR_IZQ RECUR expresionAritmetica PAR_DER
#     '''

# def p_while_statement(p):
#     '''while : PAR_IZQ WHILE comparation PAR_IZQ DO algoritmo PAR_DER
#     '''

# def p_if_statement(p):
#     '''if : PAR_IZQ IF booleanExpresion expresion expresion PAR_DER
#           | PAR_IZQ IF booleanExpresion expresion PAR_DER
#     '''

# def p_boolean_expresion(p):
#     '''booleanExpresion : FALSE
#                         | TRUE
#                         | comparationLogic
#                         | comparation
#     '''

# def p_imprimir(p):
#     '''imprimir : PAR_IZQ imprimirOptions expresion PAR_DER
#     '''

# def p_comparation_logic(p):
#     '''comparationLogic :  PAR_IZQ operadorLogic valor valor PAR_DER 
#                       | PAR_IZQ NOT valor PAR_DER
#     '''

# def p_comparation(p):
#     'comparation : PAR_IZQ operadorCompare valor valor PAR_DER'


# def p_expresion_aritmetic(p):
#     '''expresionAritmetica : PAR_IZQ operadorMath numberSerie PAR_DER
#     '''

# def p_number_serie(p):
#     '''numberSerie : numero
#                     | NOMBRE
#                     | expresionAritmetica
#                     | numero numberSerie
#                     | NOMBRE numberSerie
#                     | expresionAritmetica numberSerie
#     '''


# def p_operador_math(p):
#     '''operadorMath : SUM 
#                     | REST 
#                     | PRODUCT 
#                     | DIVISION
#     '''


# def p_operador_comparation(p):
#     '''operadorCompare : EQUAL
#                         | NOT_EQUAL
#                         | GREATER_THAN
#                         | LESS_THAN
#                         | GREATER_THAN_EQUAL
#                         | LESS_THAN_EQUAL
#     '''

# def p_operador_logic(p):
#     '''operadorLogic : AND
#                      | OR
#     '''

# def p_imprimir_options(p):
#     '''imprimirOptions : PRINT
#                         | PRINTLN
#     '''