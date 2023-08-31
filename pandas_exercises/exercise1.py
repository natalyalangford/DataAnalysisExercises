'''
Author: Natalya Langford

'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %matplotlib inline

sales = pd.read_csv(
    'data/sales_data.csv',
    parse_dates=['Date']
)

sales.head()