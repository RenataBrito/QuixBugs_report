#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import pytest

import subprocess


#local
from util import create_programs_list



def execute_python_module(algo, *args):
    """
    This function imports a given module and execute it with a list of *args parametrs then returns the execution value
    """

    #import the algorithm
    module_name = "python_programs.{}".format(algo) 
    module = __import__(module_name)    
    fx = getattr(module, algo) 

    try:

        #execute the algorithm with the *args and return the execution value
        return getattr(fx, algo)(*args)
    except:

        #whenever happens a error, show some information about it
        return sys.exc_info()


def load_tests(data):
    """
        This function handles the generation of the test data
    """    
    # Load module which contains test data
    test_data = open("json_testcases/{}.json".format(data), 'r')
    
    #for each test case in the test data
    for line in test_data:
        py_testcase = json.loads(line)
        test_in, test_out = py_testcase #get input and output values

        #create a generator to use in the test
        yield test_in, test_out 




def test_module(stringinput):
    """
        This function handles the test execution
    """

    generator = load_tests(stringinput)
    for inn, expected in generator:
        actual = execute_python_module(stringinput, inn)
        assert actual == expected




if __name__ == "__main__":
    
    algo = "bitcount"

    comando_test = 'pytest -s  --stringinput="{}"'.format(algo)
    process = subprocess.call(comando_test, shell=True)