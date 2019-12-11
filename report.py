#!/usr/bin/env python
# -*- coding: utf-8 -*-


import subprocess


#this programs need to be executed in a different way, will focus in the simple ones
graph_based = [    	"node", #node is a auxiliar object class used in the graph_based algos
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


if __name__ == "__main__":

    #pytest flags    
    """
    -vv                  #verbose mode  
    -s                   #display print outputs  
    --cov-report term    #
    --cov=python_tests/  # directory that contains the testcases
    """

    #ignore test file of the graph based algorithms 
    ignore = '--ignore=python_programs/shortest_path_length_test.py --ignore=python_programs/minimum_spanning_tree_test.py --ignore=python_programs/breadth_first_search_test.py --ignore=python_programs/depth_first_search_test.py --ignore=python_programs/detect_cycle_test.py --ignore=python_programs/reverse_linked_list_test.py --ignore=python_programs/shortest_path_lengths_test.py --ignore=python_programs/shortest_paths_test.py --ignore=python_programs/topological_ordering_test.py --ignore=python_tests_error/test_possible_change.py --ignore=python_tests_error/test_powerset.py'

    #build the command and execute

    #gera no html
    #test_comand = 'pytest {} --cov-report html -vv --cov=python_programs/'.format(ignore)
    # cobertura no terminal
    test_comand = 'pytest {} -vv -s --cov-report term  --cov=python_programs/'.format(ignore) 
    process = subprocess.call(test_comand, shell=True)