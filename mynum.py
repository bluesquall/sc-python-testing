
import numpy as np
from numpy.testing import assert_allclose

a = np.pi

def mean(num_list):
  try:
    return sum(num_list)/len(num_list)
  except ZeroDivisionError as detail:
    raise ZeroDivisionError(detail.__str__() + "\n" + 
        "Cannot calculate mean from an empty list.")

