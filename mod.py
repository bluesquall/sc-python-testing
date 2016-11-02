#!/usr/bin/env python

# example python module demonstrating test-driven development
# (see http://katyhuff.github.io/python-testing/09-tdd.html)

# Implementation:
def std(vals):
    return 1.0 # surely this is cheating...



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


