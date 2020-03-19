#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess

#used to find the root dir of the projetct
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

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
    ignore = '--ignore=working/test_shortest_path_length.py --ignore=working/test_minimum_spanning_tree.py --ignore=working/test_breadth_first_search.py --ignore=working/test_depth_first_search.py --ignore=working/test_detect_cycle.py --ignore=working/test_reverse_linked_list.py --ignore=working/test_shortest_path_lengths.py --ignore=working/test_shortest_paths.py --ignore=working/test_topological_ordering.py'

    #build the command and execute
    # --cov-report term requires pytest-cov lib

    test_comand = 'pytest {} -vv -s --cov-report term  --cov=python_programs/'.format(ignore) 
    process = subprocess.call(test_comand, shell=True)