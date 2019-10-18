#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import os
import subprocess
from util import create_programs_list




if __name__ == "__main__":
    
    if len(sys.argv) == 1:

        try:
            with open("programs.txt", "r") as programs_list:

                for program in programs_list:
                    print(program)
        except:
            create_programs_list()

   
    elif len(sys.argv) == 2:

        programa = sys.argv[1]
        
        if ".py" not in programa:
            programa += ".py"

        source_dir = ".\\quickfix\\python_programs\\"
        programa = source_dir + programa 

        comando_test = "pytest --cov . {}".format(programa)
        comando_test = "python3 {}".format(programa)
        print("Command: {}".format(comando_test))
        process = subprocess.call(comando_test, shell=True)



    
    else:
        print('W: Usage: python3 report_test.py program | python3 report_test.py ') 