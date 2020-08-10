from python_programs.node import Node

node1 = Node('1')

def test_successor():
    assert node1.successor == None

def test_successors():
    assert node1.successors == []

def test_predecessors():
    assert node1.predecessors == []