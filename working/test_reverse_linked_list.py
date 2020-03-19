from python_programs.node import Node
from python_programs.reverse_linked_list import reverse_linked_list


"""
Driver to test reverse linked list
"""
node1 = Node(1)
node2 = Node(2, node1)
node3 = Node(3, node2)
node4 = Node(4, node3)
node5 = Node(5, node4)
    
def test_5_node_list_input():
#def main():
    # Expected Output: 1 2 3 4 5
    nodeEx1 = Node(5)
    nodeEx2 = Node(4,nodeEx1)
    nodeEx3 = Node(3,nodeEx2)
    nodeEx4 = Node(2,nodeEx3)
    nodeEx5 = Node(1,nodeEx4)
    Output = nodeEx5 

    result = reverse_linked_list(node5)
    print(type(Output))
    print('\n')

    if result == node1:
        print("Reversed!", end=" ")
    else:
        print("Not Reversed!", end=" ")
    while result:
        print(result.value, end=" ")
        result = result.successor
    print()

    assert reverse_linked_list(node5) == Output


"""

    # Case 2: 1-node list input
    # Expected Output: 0
    node = Node(0)
    result = reverse_linked_list(node)

    if result == node:
        print("Reversed!", end=" ")
    else:
        print("Not Reversed!", end=" ")
    while result:
        print(result.value, end=" *")
        result = result.successor
    print()

    # Case 3: None input
    # Expected Output: None
    result = reverse_linked_list(None)
    if result == None:
        print("Reversed!", end=" ")
    else:
        print("Not Reversed!", end=" ")

    while result:
        print(result.value)
        result = result.successor
    print()
"""

if __name__ == '__main__':
    main()
    