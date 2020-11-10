from os import system
from scripts.implementation import *
import sys

if __name__ == "__main__":
    #test
    argv = sys.argv
    if len(argv)==2 and argv[1] == 'test':
        print('Running test.....')
        system("python test/test.py")

    #normal flow
    else:
        print('The best project than ever!')
    