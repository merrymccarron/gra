import os
import sys
import pandas as pd

nyvec = pd.read_csv('newyorkeryesnomatrix.csv', usecols=['UserID', 'newYorker'])

nyvec.to_csv('newyorkeryesnomatrix1.csv', index_label='index')