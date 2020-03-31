from python_programs.node import Node
from python_programs.reverse_linked_list import reverse_linked_list


def test_5_node_list_input():

    node1 = Node(1)
    node2 = Node(2, node1)
    node3 = Node(3, node2)
    node4 = Node(4, node3)
    node5 = Node(5, node4)

    #Input: 5 -> 4 -> 3 -> 2 -> 1

    result = reverse_linked_list(node5)

    #Expected Output: 1 2 3 4 5

    #Para que possa fazer um assert é preciso criar uma string com esse modelo
    expected_output = '1 2 3 4 5 '

    #agora vemos qual a string que result produz
    string_result = ''
    while result:
        string_result += str(result.value) + ' '
        result = result.successor
        
    assert string_result == expected_output



def test_1_node_list_input():

    # Case 2: 1-node list input
    # Expected Output: 0
    node = Node(0)
    result = reverse_linked_list(node)

    expected_output = '0 '

    #agora vemos qual a string que result produz
    string_result = ''
    while result:
        string_result += str(result.value) + ' '
        result = result.successor

    #por fim fazemos o assert
    assert string_result == expected_output


def test_none_input():
    # Case 3: None input
    # Expected Output: None
    result = reverse_linked_list(None)
    
    expected_output = ''

    #agora vemos qual a string que result produz
    string_result = ''
    while result:
        string_result += str(result.value) + ' '
        result = result.successor

    #por fim fazemos o assert
    assert string_result == expected_output
