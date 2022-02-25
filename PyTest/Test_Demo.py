import math
import pytest
def square_root(x):
    return math.sqrt(x)

def test_solution():
    assert square_root(64)==8

def cube(y):
    return y*y*y

def test_cube():
    assert cube(3)==27

def power(z):
    return 5**z

def test_power():
    assert power(2)==25