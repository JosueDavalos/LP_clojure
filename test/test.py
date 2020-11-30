import sys
sys.path.append(".")

from scripts.implementation import *



argv = sys.argv
name_file = argv[-1]


def run_test(file):
    print('Running test..... %s'%file.upper())

    test = open('test/%s'%file, 'r', encoding="utf8")
    for line in test:
        setencia  = line.strip()
        if len(setencia)!=0 : 
            print('-'*0,setencia,'-'*0,end='  ==>>   ')
            # t_analizar_lexico(setencia)
            t_analizar_sintaxis(setencia)
            
run_test(name_file)
