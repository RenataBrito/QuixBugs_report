import sys
sys.path.append('../')
import bitcount

#sys.path.insert(0, '/Desktop/teste/a')
from bitcount import bitcount
#from bitcount import bitcount

def test():
    assert bitcount(127) == 7

def test2():
    assert bitcount(128) == 1
