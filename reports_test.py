#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import pytest

import copy
import types
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
        
        #in order to garantee copy operation always take inputs as a list
        if not isinstance(inn, list):
            inn = [inn]
        
        # *copy.deepcopy(inn) to pass arguments separable
        actual = execute_python_module(stringinput, *copy.deepcopy(inn))
        
        #some programs produces a generator and the json file expects a list. Thus convert the generator into a list to perform the assertion
        if isinstance(actual, types.GeneratorType):
            actual = list(actual)        
        
        print('Input: ', inn)
        print('Actual: ', actual, '| Expected: ', expected)
        assert actual == expected




if __name__ == "__main__":
    
    #this programs need to be executed in a different way, will focus in the simple ones
    graph_based = ["node", #node is a auxiliar object class used in the graph_based algos
               "breadth_first_search",
               "depth_first_search",
               "detect_cycle",
               "minimum_spanning_tree",
               "reverse_linked_list",
               "shortest_path_length",
               "shortest_path_lengths",
               "shortest_paths",
               "topological_ordering"
              ]

    #run a single algo specified through parameter
    if len(sys.argv) == 2:

        algo = sys.argv[1]

        """
            -m loads pytest module
            -vv #verbose mode
            -s shows print statments 
            --timeout= 60 #time in seconds
            --cov-branch
            --cov-report term  
        """
        test_comand = 'python3 -m pytest -vv -s  --timeout=20 --stringinput="{}"'.format(algo)
        process = subprocess.call(test_comand, shell=True)

    #run all algorithms
    else:

        with open('programs.txt', 'r') as algo_list:

            for algo in algo_list:

                #skips \n and .py
                algo = algo[:-4]

                #skip the programs that don't have json testcases 
                if algo not in graph_based:
                    

                    """
                        -m loads pytest module
                        -s shows print statments 
                    """
                    test_comand = 'python3 -m pytest -vv -s --timeout=20 --stringinput="{}"'.format(algo)
                    process = subprocess.call(test_comand, shell=True)  