
from python_programs.node import Node
from python_programs.shortest_path_length import shortest_path_length


node1 = Node("1")
node5 = Node("5")
node4 = Node("4", None, [node5])
node3 = Node("3", None, [node4])
node2 = Node("2", None, [node1, node3, node4])
node0 = Node("0", None, [node2, node5])

length_by_edge = {
    (node0, node2): 3,
    (node0, node5): 10,
    (node2, node1): 1,
    (node2, node3): 2,
    (node2, node4): 4,
    (node3, node4): 1,
    (node4, node5): 1
}

def test_One_path():
    assert shortest_path_length(length_by_edge, node0, node1) == 4

def test_Multiple_path():
    assert shortest_path_length(length_by_edge, node0, node5) == 7

def test_Start_point_is_same_as_end_point():
    assert shortest_path_length(length_by_edge, node2, node2) == 0

def test_Unreachable_path():
    assert shortest_path_length(length_by_edge, node1, node5) == float('inf')

def test_nextnode_in_visited_nodes():
    node5 = Node("5")
    node4 = Node("4", None, [node5])
    node3 = Node("3", None, [node4])
    node1 = Node("1",None,  [node4, node3, node5])
    node2 = Node("2", None, [node1, node3, node4])
    node0 = Node("0", None, [node2, node5])

    length_by_edge = {
        (node0, node2): 3,
        (node0, node5): 10,
        (node1, node4): 7,
        (node1, node3): 8,
        (node1, node5): 9,
        (node2, node1): 5,
        (node2, node3): 2,
        (node2, node4): 4,
        (node3, node4): 1,
        (node4, node5): 1
    }

    assert shortest_path_length(length_by_edge, node0, node5) == 7

