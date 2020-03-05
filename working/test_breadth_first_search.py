#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import pytest

from pytest_report import ROOT_DIR

from python_programs.node import Node
from python_programs.breadth_first_search import breadth_first_search



def test_strongly_connected_graph():

    # Output: Path found!
    station1 = Node("Westminster")
    station2 = Node("Waterloo", None, [station1])
    station3 = Node("Trafalgar Square", None, [station1, station2])
    station4 = Node("Canary Wharf",  None, [station2, station3])
    station5 = Node("London Bridge",  None, [station4, station3])
    station6 = Node("Tottenham Court Road",  None, [station5, station4])
    
    
    if breadth_first_search(station6, station1):
        print("Path found!", end=" ")
    else:
        print("Path not found!", end=" ")
    print()



def test_branching_graph():

    # Output: Path found!
    nodef =  Node("F")
    nodee =  Node("E")
    noded =  Node("D")
    nodec =  Node("C", None, [nodef])
    nodeb =  Node("B", None, [nodee])
    nodea =  Node("A", None, [nodeb, nodec, noded])

    if breadth_first_search(nodea, nodee):
        print("Path found!", end=" ")
    else:
        print("Path not found!", end=" ")
    print()



def test_two_unconnected_nodes_in_graph():
    
    # Output: Path not found

    nodef =  Node("F")
    nodee =  Node("E")
    noded =  Node("D")
    nodec =  Node("C", None, [nodef])
    nodeb =  Node("B", None, [nodee])
    nodea =  Node("A", None, [nodeb, nodec, noded])
        
    if breadth_first_search(nodef, nodee):
        print("Path found!", end=" ")
    else:
        print("Path not found!", end=" ")
    print()


def test_one_node_graph():
    
    # Output: Path found!

    nodef =  Node("F")
    nodee =  Node("E")
    noded =  Node("D")
    nodec =  Node("C", None, [nodef])
    nodeb =  Node("B", None, [nodee])
    nodea =  Node("A", None, [nodeb, nodec, noded])
    
    if breadth_first_search(nodef, nodef):
        print("Path found!", end=" ")
    else:
        print("Path not found!", end=" ")
    print()



def test_graph_with_cycles():

    # Output: Path found!

    #setup
    node1 = Node("1")
    node2 = Node("2")
    node3 = Node("3")
    node4 = Node("4", None, [node1])
    node5 = Node("5", None, [node2])
    node6 = Node("6", None, [node5, node4, node3])

    node2.successors = [node6]

    #exercice
    if breadth_first_search(node6, node1):
        print("Path found!", end=" ")
    else:
        print("Path not found!", end=" ")
    print()

    #verify
    

    #cleanup