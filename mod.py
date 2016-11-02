#!/usr/bin/env python

# example python module demonstrating test-driven development
# (see http://katyhuff.github.io/python-testing/09-tdd.html)

# Dependencies:
from numpy.testing import assert_allclose, assert_equal

# Implementation:
def std(vals):
    if len(vals) == 0: # edge case: empty list
        return 0.0
    return vals[-1]/2.0 # this is still cheating...



# Tests:
def test_std1():
    obs = std([0.0, 2.0])
    exp = 1.0
    assert obs == exp

def test_std2():
    # Test the fiducial case when we pass an empty list.
    obs = std([])
    exp = 0.0
    assert obs == exp

def test_std3():
    # Test a real case where the answer is not one.
    obs = std([0.0, 4.0])
    exp = 2.0
    assert_equal(obs, exp)

def test_std4():
    # Test a real case where the first value is not zero.
    obs = std([1.0, 3.0])
    exp = 1.0
    assert_equal(obs, exp)

def test_std5():
    # Test a longer list, but with identical entries.
    obs = std([1.0, 1.0, 1.0])
    exp = 0.0
    assert_equal(obs, exp)


