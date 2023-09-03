'''
Function that uses Numpy to:
  - convert list to a 3 x 3 Matrix 
  - returns dictionary containing
    - mean
    - variance
    - standard deviation
    - max
    - min
    - sum of rows
    - sum of columns
    - sum of elements
  
'''

import numpy as np


# list: [0,1,2,3,4,5,6,7,8]
def calculate(list):
  if len(list) < 9:
    raise ValueError("List must contain nine numbers.")

  
  # use numpy to store list
  matrix = np.array(list)

  # convert list to 3 x 3 matrix
  matrix = matrix.reshape(3, 3)

  # init dictionary to return
  calculations = {
    # 'xxxx': [axis1, axis2, flattened]
    'mean': [None, None, None],
    'variance': [None, None, None],
    'standard deviation': [None, None, None],
    'max': [None, None, None],
    'min': [None, None, None],
    'sum': [None, None, None]
  }
  
  calculations['mean'] = [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean().tolist()] # store mean for axis1
  calculations['variance'] = [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.mean().tolist()]
  calculations['standard deviation'] = [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.mean().tolist()]
  calculations['max'] = [matrix.max(axis=0).tolist(), matrix.max(axis=0).tolist(), matrix.max().tolist()]
  calculations['min'] = [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min().tolist()]
  calculations['sum'] = [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum().tolist()]


  calculations

  return calculations
