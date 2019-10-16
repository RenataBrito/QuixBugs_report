#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import os
import subprocess
#from quickfix.python_programs import *




if __name__ == "__main__":
    #a = bitcount.bitcount(5)
    
    if len(sys.argv) == 2:
        #executar com todos
        programa = sys.argv[1]
        #comando = "{}".format(programa)
        comando = "python3 {}".format(programa)
        out_str = subprocess.check_output(comando, shell=True)

        print(out_str)

    elif len(sys.argv) == 3:
        #executar so com 1
        #programas = util.create_programs

        #for programa in programs:
            #comando = "python3 {}".format(programa)
            #os.exec(comando)
        pass
    else:
        print('W: Usage: python3 report_test.py program | python3 report_test.py ') 