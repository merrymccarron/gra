# 54953 users from the (recent) Search API (out of ~288000) are in our social landmark followers lists (any)
# ~19%

#create a dictionary to store the userid and who they follow?

import os
import sys
import bisect
import pandas as pd
import glob


followeridsdf = pd.DataFrame(data={'UserID': []})

for followersfile in glob.glob('sociallandmarks/*followerids.csv'):
	tempfile = pd.read_csv(followersfile, index_col=0)
	followeridsdf = followeridsdf.append(tempfile)

followeridsdf = followeridsdf.drop_duplicates
followerslist = followeridsdf['UserID'].values.tolist()
followerslistsorted = sorted(followerslist)
# print len(followerslist)
# print type(followerslistsorted)
# print 'followers id dataframe for all social landmarks:'
# print followeridsdf.shape
##### CHECK TO SEE FORMAT OF FOLLOWERS IDS

data = {'Tweet ID': [], 'UserID': [], 'Location': [], 'Geo': []}
tweetdf = pd.DataFrame(data)

for csvfile in glob.glob('newcsvs/*.csv'):
	tempfile = pd.read_csv(csvfile, usecols=['Tweet ID', 'UserID', 'Location', 'Geo'])
	tweetdf = tweetdf.append(tempfile)
tweetdf['Tweet ID'] = tweetdf['Tweet ID']
tweetdf['UserID'] = tweetdf['UserID']
# print 'Done'
# print tweetdf.shape

tweetuserids = tweetdf['UserID']
# ##CHECK TO SEE FORMAT OF FOLLOWER IDS
# print tweetuserids.head(5)


def binary_search(L, v):
  lengthOfL = len(L)
  imin = 0
  imax = lengthOfL # imax always points to end of array (non inclusive).
  while imin < imax:
    # Computes midpoint for roughly equal partition.
    imid = int((imin + imax) / 2)
    if v == L[imid]:   # v found at index imid.
      return L[imid]
      break
    elif v < L[imid]:  # Changes imax index to search lower subarray.
      imax = imid
    else:              # Changes imin index to search upper subarray.
      imin = imid + 1
 
  if imin < imax:      # Found v
    # Handles repetitions: makes imid point to 1st greater than v.
    while imid < lengthOfL and v == L[imid]:
      imid += 1
    # Return userid
    # return L[imid]
    return True
  else:
    # if userid isn't in list, return -1
    # return -1
    return False

usersinsociallandmark = []

for tweetuserid in tweetuserids:
	binsearchresult = binary_search(followerslistsorted, tweetuserid)
	if binsearchresult != -1:
		# print binsearchresult
		usersinsociallandmark.append(binsearchresult)

print len(usersinsociallandmark)

df = pd.DataFrame(data={'UserID': usersinsociallandmark})

# df.to_csv('sociallandmarkssearchAPIusersFollowingSL.csv', header=True)






