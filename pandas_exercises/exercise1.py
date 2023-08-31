'''
Author: Natalya Langford

'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# initialize data for pandas 
sales = pd.read_csv(
'data/sales_data.csv',
parse_dates=['Date'])

    
def info():
    print(sales.head()) # display the first few rows of a DataFrame
    
    print("Total Rows: {}  & Columns: {}".format(sales.shape[0], sales.shape[1]))
    print()
    print("Data Frame Info: ")
    sales.info() # displays info about data frame 
    
    
# call functions
info()