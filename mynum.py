
import numpy as np
from numpy.testing import assert_allclose

a = np.pi

def mean(num_list):
  assert len(num_list) > 0
  assert isinstance(num_list, list)
  return sum(num_list)/len(num_list)


