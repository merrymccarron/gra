import os
import sys
import pandas as pd
import glob

csvcount = 0
data = {'Tweet ID': [], 'UserID': [], 'Location': [], 'Geo': []}
df = pd.DataFrame(data)

for csvfile in glob.glob('newcsvs/*.csv'):
	tempfile = pd.read_csv(csvfile, usecols=['Tweet ID', 'UserID', 'Location', 'Geo'])
	df = df.append(tempfile)
	csvcount +=1
	# print csvcount
	# print csvfile
# df = df[df.Place != None]
# df = df.drop_duplicates(['Tweet ID'])
df['Tweet ID'] = df['Tweet ID'].astype(basestring)
df['UserID'] = df['UserID'].astype(basestring)
df.to_csv('concat.csv', header=True, float_format = "%.0f", columns=['Tweet ID', 'UserID', 'Location', 'Geo'], engine='python')
print 'Done'
print df.shape
print df.dtypes