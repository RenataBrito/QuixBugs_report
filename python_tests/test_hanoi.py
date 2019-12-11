#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import pytest

from python_programs.hanoi import hanoi


#open 
json_file = open('json_testcases/hanoi.json', 'r')

testcases = [tuple(json.loads(line)) for line in json_file]

#example of model extracted from the json file -> A list which every single element is a tuple(input, output)
"""parametrize expects a object such as: [
    ('banana', 0),
    ('water', 1),
    ('Apples', 1),
    ('apple', 1),
    ('le', 2),
    ('zZ', 1),
    ('e', 5),
]"""

@pytest.mark.parametrize("test_input,expected", testcases)
def test_hanoi(test_input, expected):
    generator_output = hanoi(*test_input)

    #must convert into a list before the assertion
    output = list(generator_output)
    newList =[]
    for tupla in output:
        a = list(tupla)
        newList.append(a)
    assert  newList == expected
    #assert hanoi(*test_input) == expected