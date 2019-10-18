import os
import sys

from quickfix.python_programs import bitcount
from quickfix.python_programs import gcd


def test1():
    
    #k = os.chdir(".quickfix.json_testcases")
    #print(k)
    #with open() as test_input:
    assert bitcount.bitcount(127) == 7

def test2():
    assert bitcount.bitcount(128) == 1

def test3():
    assert gcd.gcd(17,0) == 17

def test4():
    assert gcd.gcd(13,13) == 13