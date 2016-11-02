import os
from numpy.testing import assert_allclose, assert_equal
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

def test_fib0():
  # test edge 0
  assert fib(0) == 1

def test_fib1():
  assert fib(1) == 1

def test_fib6():
  assert fib(6) == 13

def test_fib_negative():
  assert fib(-1) == NotImplemented

def test_fib_fraction():
  assert fib(2.5) == NotImplemented

def test_sinc2d_internal():
  exp = (2.0 / np.pi) * (-2.0 / (3.0 * np.pi))
  obs = sinc2d(np.pi / 2.0, 3.0 * np.pi / 2.0)
  assert obs == exp

def test_sinc2d_edge_x():
  exp = -2.0 / (3.0 * np.pi)
  obs = sinc2d(0, 3 * np.pi / 2)
  assert obs == exp

def test_sinc2d_edge_y():
  exp = 2.0 / np.pi
  obs = sinc2d(np.pi / 2, 0)
  assert obs == exp

def test_sinc2d_corner():
  exp = 1.0
  obs = sinc2d(0, 0)
  assert obs == exp


# An integration test:
def test_mean_fib_0():
  assert mean_fib(0) == 1

def test_mean_fib_6():
  assert_allclose(mean_fib(6), 4.714286, atol=1e-6)

def test_mean_fib_neg():
  assert mean_fib(-1) == 0

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

def setup_function(func):
    files = os.listdir('.')
    if 'no.txt' in files:
        os.remove('no.txt')
    if 'yes.txt' in files:
        os.remove('yes.txt')

def teardown_function(func):
    if 'yes.txt' in os.listdir('.'):
        os.remove('yes.txt')

def test_write_num():
    exp = 42
    write_num(exp)
    with open('yes.txt', 'r') as fh:
        obs = int(fh.read())
    assert obs == exp



