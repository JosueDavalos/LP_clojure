from os import system
from scripts.interfaz import *
import sys

if __name__ == "__main__":
    #test
    argv = sys.argv
    if len(argv)==3 and argv[1] == 'test':
        out = system("python test/test.py %s"%argv[2])
        if out !=0 :
            system("python3 test/test.py %s"%argv[2])

    #normal flow
    else:
        app = tk.Tk()
        window = Window(app)
        app.mainloop()
    
