from mynum import *

def test_ints():
  num_list = [1, 2, 3, 4, 5]
  obs = mean(num_list)
  exp = 3
  assert obs == exp

def test_zero():
  num_list = [0, 2, 4, 6]
  obs = mean(num_list)
  exp = 3
  assert obs == exp

def test_double():
  # This one will fail in Python 2...
  num_list = [1, 2, 3, 4]
  obs = mean(num_list)
  exp = 2.5
  assert obs == exp

def test_long():
  big = 100000000
  obs = mean(range(1,big))
  exp = 0.5 * big
  assert obs == exp

# skipping test_complex, because the lesson's assertion that "the arithmetic mean of complex numbers is meaningless" is not true

