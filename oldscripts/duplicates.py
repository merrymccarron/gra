import os
import sys
import pandas as pd
import glob

df = pd.read_csv('concat.csv')

print df.shape

df = df.drop_duplicates(['Tweet ID'])

print df.shape

df.to_csv('concat.csv')