#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import pytest

from pytest_report import ROOT_DIR
from python_programs.possible_change import possible_change


#open 
json_file = open(ROOT_DIR + '/json_testcases/possible_change.json', 'r')

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
def test_possible_change(test_input, expected):
    assert possible_change(*test_input) == expected