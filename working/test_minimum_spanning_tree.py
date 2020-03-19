from python_programs.minimum_spanning_tree import minimum_spanning_tree


"""
Driver to test minimum spanning tree
"""
def test_Simple_tree_input():
    Output = {(1, 2) ,(3, 4), (1, 4)}
    assert minimum_spanning_tree({
        (1, 2): 10,
        (2, 3): 15,
        (3, 4): 10,
        (1, 4): 10}) == Output

def test_Strongly_connected_tree_input():
    Output = {(2, 5),(1, 3),(2, 3),(4, 6),(3, 6)}
    assert minimum_spanning_tree({
        (1, 2): 6,
        (1, 3): 1,
        (1, 4): 5,
        (2, 3): 5,
        (2, 5): 3,
        (3, 4): 5,
        (3, 5): 6,
        (3, 6): 4,
        (4, 6): 2,
        (5, 6): 6}) == Output

def test_Minimum_spanning_tree_input():
    Output = {(1, 2), (1, 3), (2, 4)}
    assert minimum_spanning_tree({
            (1, 2): 6,
            (1, 3): 1,
            (2, 4): 2}) == Output




