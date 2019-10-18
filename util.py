#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os 
import sys


def create_programs_list():

    source = '.\\quickfix\\python_programs'

    for root, dirs, files in os.walk(source, topdown=False):
        #for directory in dirs:
        for f in files:
            if f[-3:] == '.py':
                with open('programs.txt', 'a') as programs_file:
                    name = "{}\n".format(f)
                    programs_file.write(name)