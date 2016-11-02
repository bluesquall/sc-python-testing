
import numpy as np
from numpy.testing import assert_allclose

a = np.pi

def mean(num_list):
  try:
    return sum(num_list)/len(num_list)
  except ZeroDivisionError:
    return 0
  except TypeError as detail:
    raise TypeError(detail.__str__() + "\n"
        + "Cannot calculate the mean of a non-numerical list.")

def fib(n):
  if n == 0 or n == 1:
    return 1
  elif isinstance(n, int):
    if n > 0:
      return fib(n - 1) + fib(n - 2)
    else:
      return NotImplemented #Error("Fibonacci sequence doesn't include negatives.")
  else:
    return NotImplemented #Error("Fibonacci sequence only defined for integers.")

def mean_fib(n):
  return mean([fib(m) for m in range(n+1)])

def sinc2d(x, y):
  if x == 0:
    if y == 0:
      return 1.0
    else:
      return np.sin(y) / y
  elif y == 0:
    return np.sin(x) / x
  else:
    return np.sin(x) / x * np.sin(y) / y

def sinc2d_ex(x, y):
  try:
    return np.sin(x) / x * np.sin(y) / y
  except ZeroDivisionError:
    try:
      return np.sin(x) / x
    except ZeroDivisionError:
      try:
        return np.sin(y) / y
      except ZeroDivisionError:
        return 1.0

def std(vals):
    if len(vals) == 0: # edge case: empty list
        return 0.0
    mu = mean(vals)
    var = 0.0
    for x in vals:
        var += (x - mu)**2
    var /= len(vals)
    return (var)**0.5

