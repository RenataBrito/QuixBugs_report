from python_programs.node import Node
from python_programs.detect_cycle import detect_cycle


"""
Driver to test reverse linked list
"""

node1 = Node(1)
node2 = Node(2, node1)
node3 = Node(3, node2)
node4 = Node(4, node3)
node5 = Node(5, node4)
def test_5_node_list_input_with_no_cycle():
    assert detect_cycle(node5) == False

def test_5_node_list_input_with_cycle():
    node1.successor = node5
    assert detect_cycle(node5) == True

def test_2_node_list_with_cycle():
    node1.successor = node2
    assert detect_cycle(node2) == True

def test_2_node_list_with_no_cycle():
    node6 = Node(6)
    node7 = Node(7, node6)
    assert detect_cycle(node7) == False

def test_1_node_list():
    node = Node(0)
    assert detect_cycle(node) == False


