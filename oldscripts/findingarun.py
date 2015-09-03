import sys
import os
import pandas as pd

matrix = pd.read_csv('matrix.csv', index_col='UserID')

print matrix.loc[27922176,:]