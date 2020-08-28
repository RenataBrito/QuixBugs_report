from node import Node


def test_successor():
    n     = Node(value = 2)
    node1 = Node(value = 1, successor= n)
        
    node3 = node1.successor

    assert n.value == node3.value

def test_successors():

    n     = Node(value = 2)
    n2    = Node(value = 3)
    node1 = Node(value = 1, successors = [n, n2])
        
    node3 = node1.successors[0]

    assert len(node1.successors) == 2

def test_predecessors():

    n     = Node(value = 2)
    n2    = Node(value = 3)
    n3    = Node(value = 4)
    node1 = Node(value = 1, predecessors = [n, n2, n3])
        
    node3 = node1.predecessors[0]

    assert len(node1.predecessors) == 3
