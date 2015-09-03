import os
import sys
import pandas as pd
import numpy as np
import glob

allUserIDs = pd.read_csv('concat.csv', usecols = ['UserID'], error_bad_lines = False, 
    warn_bad_lines = True).drop_duplicates(['UserID'])

allUserIDs = allUserIDs['UserID'].values

numberOfSocialLandmarks = 0
socialLandmarkFollowers = []
socialLandmarkNames = []
# socialLandmarkFollowers = {}
for csvfile in glob.glob('sociallandmarks/*followerids.csv'):
    # socialLandmarkFollowers.append(pd.read_csv('csvfile', colnames = csvfile.strip('followerids.csv')))
    socialLandmarkHandle = csvfile[16:-15]
    socialLandmarkNames.append(socialLandmarkHandle)
    df = pd.read_csv(csvfile, usecols=['UserID']).drop_duplicates(['UserID'])
    # socialLandmarkFollowers[socialLandmarkHandle] = df['UserID'].values.tolist()
    # socialLandmarkFollowers.append([socialLandmarkHandle, df['UserID'].values.tolist()])
    socialLandmarkFollowers.append([socialLandmarkHandle, df['UserID'].values])
    # allUserIDs.append(df['UserID'].values)
    np.concatenate((allUserIDs, df['UserID'].values), axis=1)
    numberOfSocialLandmarks += 1

numberOfUserIDs = len(allUserIDs)

sortedUserIDs = sorted(allUserIDs)

print np.where(sortedUserIDs==2571632905.0)
print numberOfUserIDs