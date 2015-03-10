import os
import sys
import bisect
import pandas as pd
import glob


followeridsdf = pd.read_csv('gothamistfollowerids.csv')
followerslist = followeridsdf['UserID'].tolist()
followerslistsorted = followerslist.sorted()
# print followerslist

# data = {'UserID' : []}
# tweetsdf = pd.DataFrame(data)
# tweetsdf = pd.read_csv('csv_tweets2015-03-03_15-51-05.csv')


# tweetuserids = tweetsdf['UserID']

data = {'Tweet ID': [], 'UserID': [], 'Location': [], 'Geo': []}
tweetdf = pd.DataFrame(data)

for csvfile in glob.glob('newcsvs/*.csv'):
	tempfile = pd.read_csv(csvfile, index_col=1, usecols=['Tweet ID', 'UserID', 'Location', 'Geo'])
	tweetdf = tweetdf.append(tempfile)
print 'Done'
print df.shape




def binary_search(a, x, lo=0, hi=None):   # can't use a to specify default for hi
    hi = hi if hi is not None else len(a) # hi defaults to len(a)   
    pos = bisect.bisect_left(a,x,lo,hi)          # find insertion position
    return (pos if pos != hi and a[pos] == x else -1)


# def bin_search_followers(followerslist):
# 	for tweetuserid in tweetuserids:
# 		binary_search(tweetuserid, followerslist, lo=0, high=None)

for tweetuserid in tweetuserids:
	binsearchresult = binary_search(followerslist, tweetuserid, lo=0, hi=None)

print binsearchresult