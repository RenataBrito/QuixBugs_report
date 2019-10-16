#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os 
import sys

if __name__ == "__main__":
    
    source = '.\\quickfix\\python_programs'

    for root, dirs, files in os.walk(source, topdown=False):
        #for directory in dirs:
        for f in files:
            if '.py' not in f:
                print('entro no not')
                pass
            else:  
                with open('programs.txt', 'a') as programs_file:
                    name = "{}\n".format(f)
                    programs_file.write(name)
