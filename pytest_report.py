#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess

#used to find the root dir of the projetct
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


if __name__ == "__main__":

    #pytest flags    
    """
    -vv                  #verbose mode  
    -s                   #display print outputs  
    --cov-report term    #
    --cov-report html    #
    --cov=python_tests/  # directory that contains the testcases
    """

    #build the command and execute
    # --cov-report term or --cov-report html requires pytest-cov lib

    #exit at the terminal
    #test_comand = 'pytest -vv -s --cov-report term  --cov=python_programs/' 

    #exit on web page
    test_comand = 'pytest -vv -s --cov-report html  --cov=python_programs/'
    
    process = subprocess.call(test_comand, shell=True)