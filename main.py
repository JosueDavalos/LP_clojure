from os import system
from scripts.implementation import *
import sys

if __name__ == "__main__":
    #test
    argv = sys.argv
    if len(argv)==3 and argv[1] == 'test':
        system("python test/test.py %s"%argv[2])

    #normal flow
    else:
        print('The best project than ever!')
    