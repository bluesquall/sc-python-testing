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