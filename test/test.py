import sys
sys.path.append(".")

from scripts.implementation import *


list_types = '''
true false
1 0 11 5697
"hola mundo" "hola"mundo"
:key1 :keyss 
'(1 2 3 4 4) 
#(1 2 4 4)
{:hola "mundo"}
'''




def run_test():
    t_analizar('if')

run_test()