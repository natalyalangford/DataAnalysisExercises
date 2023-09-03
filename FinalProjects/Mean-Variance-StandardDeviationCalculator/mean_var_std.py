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
  
  # store by indexing 
  calculations['mean'][0] = np.mean(matrix, axis=0)  # store mean for axis1
  calculations['mean'][1] = np.mean(matrix, axis=1)  
  calculations['mean'][2] = np.mean(matrix)
  
  # or store directly 
  calculations['variance'] = [np.var(matrix, axis=0), np.var(matrix, axis=1), np.var(matrix)]
  calculations['standard deviation'] = [np.std(matrix, axis=0), np.std(matrix, axis=1), np.std(matrix)]
  calculations['max'] = [np.max(matrix, axis=0), np.max(matrix, axis=1), np.max(matrix)]
  calculations['min'] = [np.min(matrix, axis=0), np.min(matrix, axis=1), np.min(matrix)]
  calculations['sum'] = [np.sum(matrix, axis=0), np.sum(matrix, axis=1), np.sum(matrix)]


  calculations

  return calculations
