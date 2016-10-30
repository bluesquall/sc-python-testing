
import numpy as np
from numpy.testing import assert_allclose

a = np.pi

def mean(num_list):
  if len(num_list) == 0:
    raise Exception("Cannot calculate mean from an empty list.")
  else:
    return sum(num_list)/len(num_list)


