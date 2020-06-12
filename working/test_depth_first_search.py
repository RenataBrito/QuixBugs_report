from python_programs.node import Node
from python_programs.depth_first_search import depth_first_search

nodef =  Node("F")
nodee =  Node("E")
noded =  Node("D")
nodec =  Node("C", None, [nodef])
nodeb =  Node("B", None, [nodee])
nodea =  Node("A", None, [nodeb, nodec, noded])


def test_strongly_connected_graph():
    station1 = Node("Westminster")
    station2 = Node("Waterloo", None, [station1])
    station3 = Node("Trafalgar Square", None, [station1, station2])
    station4 = Node("Canary Wharf",  None, [station2, station3])
    station5 = Node("London Bridge",  None, [station4, station3])
    station6 = Node("Tottenham Court Road",  None, [station5, station4])

    assert depth_first_search(station6, station1) == True

def test_branching_graph():
    assert depth_first_search(nodea, nodee) == True

def test_two_unconnected_nodes_in_graph():
    assert depth_first_search(nodef, nodee) == False

def test_one_node_graph():
    assert depth_first_search(nodef, nodef) == True

def test_graph_with_cycles():
    assert depth_first_search(nodea, nodef) == True

def test_recente():
    station1 = Node("Westminster")
    station2 = Node("Waterloo", None, [station1])   
    station3 = Node("Trafalgar Square", None, [station1, station2])
    station4 = Node("Canary Wharf",  None, [station2, station3])

    assert depth_first_search(station3, station4) == False