import sys
from scripts.implementation import *

sys.path.append(".")

argv = sys.argv
name_file = argv[-1]


def run_test(file):
    print('Running test..... %s'%file.upper())

    test = open('test/%s'%file, 'r', encoding="utf8")
    for line in test:
        setencia  = line.strip()
        if len(setencia)!=0 : 
            print('-'*5,setencia,'-'*5)
            # t_analizar_lexico(setencia)
            t_analizar_sintaxis(setencia)
            print()

run_test(name_file)