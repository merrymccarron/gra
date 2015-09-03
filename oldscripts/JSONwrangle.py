import sys
import os
import json
import pandas as pd

jsondf = pd.read_table('json_tweetsDec_26_2014_02_52.txt', header=None)

print jsondf.head(2)
print jsondf.shape

mylist = [1, 4, 6, 3]

test = jsondf[0].tolist()
# testjsonload = json.loads(test[0])
print test[0:2]
# print jsondf.dtypes

# print list(jsondf.columns.values)

