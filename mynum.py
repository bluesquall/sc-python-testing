
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

