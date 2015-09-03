# -*- coding: utf-8 -*-
"""
need to create a 16 x 1 million (or so, or however users I have) matrix, 
where each user is represented with a length 16 numpy array of 1s and 0s, standing 
for whether they follow each of the social landmarks. Also add a 1 million long numpy 
array of Trues and Falses, standing for whether they are a 'new yorker' by our 
estimation, and finally another million-long numpy array of the UserIDs. Obviously, 
these all need to be ordered the same way.
"""
import os
import sys
import pandas as pd
import numpy as np
import glob
import datetime
import string
from binarysearch import binary_search

GAZETTEER = ['gotham', 'new york', "NY,NY", 'new york city', 'nyc', 'brooklyn', 'bkln', 'bronx', 'staten island', 'si', 'queens', 'manhattan', 'greenpoint', 'williamsburg', 'boerum hill', 'brooklyn heights', 'brooklyn navy yard', 'clinton hill', 'dumbo', 'fort greene', 'vinegar hill', 'bedford-stuyvesant', 'bed stuy', 'bed-stuy', 'stuyvesant heights', 'bushwick', 'cypress hills', 'east new york', 'highland park', 'new lots', 'carroll gardens', 'cobble hill', 'gowanus', 'park slope', 'south slope', 'red hook', 'greenwood heights', 'sunset park', 'windsor terrace', 'crown heights', 'prospect heights', 'lefferts gardens', 'bay ridge', 'dyker heights', 'fort hamilton', 'bensonhurst', 'gravesend', 'borough park', 'kensington','midwood', 'brighton beach', 'coney island', 'flatbush', 'sheepshead bay','brownsville', 'east flatbush', 'bergen beach', 'canarsie', 'battery park city', 'financial district', 'tribeca', 'chinatown', 'greenwich village', 'little italy', 'lower east side', 'noho', 'soho', 'west village', 'alphabet city', 'chinatown', 'east village', 'two bridges', 'chelsea', 'clinton', 'hell\'s kitchen', 'hells kitchen','midtown', 'gramercy park', 'grammercy', 'kips bay', 'murray hill', 'peter cooper village', 'stuyvesant town', 'stuy town', 'sutton place','tudor city', 'turtle bay', 'waterside plaza', 'upper west side', 'lenox hill', 'roosevelt island', 'upper east side', 'yorkville', 'hamilton heights', 'manhattanville', 'morningside heights', 'harlem', 'east harlem', 'spanish harlem', 'randall’s island', 'inwood', 'washington heights', 'astoria', 'ditmars', 'garden bay', 'long island city', 'queensbridge', 'ravenswood', 'steinway', 'woodside', 'sunnyside', 'hunters point', 'elmhurst', 'jackson heights', 'corona', 'roosevelt avenue', 'fresh pond', 'glendale', 'maspeth', 'middle village', 'liberty park', 'ridgewood', 'forest hills', 'rego park', 'bay terrace', 'beechhurst', 'college point', 'flushing', 'linden hill', 'malba', 'queensboro hill', 'whitestone', 'willets point', 'briarwood', 'cunningham heights', 'flushing', 'fresh meadows', 'hilltop village', 'holliswood', 'jamaica estates', 'kew gardens hills', 'pomonok houses', 'utopia', 'kew gardens', 'ozone park', 'richmond hill', 'woodhaven', 'howard beach', 'lindenwood', 'tudor village', 'auburndale', 'bayside', 'douglaston', 'east flushing', 'hollis hills', 'little neck', 'oakland gardens', 'baisley park', 'jamaica', 'hollis', 'rochdale village', 'st. albans', 'springfield gardens', 'bellerose', 'brookville', 'cambria heights', 'floral park', 'glen oaks', 'laurelton', 'meadowmere', 'new hyde park', 'queens village', 'rosedale', 'arverne', 'bayswater', 'belle harbor', 'breezy point', 'edgemere', 'far rockaway', 'neponsit', 'rockaway park', 'arlington', 'castleton corners', 'clifton', 'concord', 'elm park', 'fort wadsworth', 'graniteville', 'grymes hill', 'livingston', 'mariners harbor', 'meiers corners', 'new brighton', 'port ivory', 'port richmond', 'randall manor', 'rosebank', 'st. george', 'shore acres', 'silver lake', 'stapleton', 'tompkinsville', 'west brighton', 'westerleigh', 'arrochar', 'bloomfield', 'bulls heads', 'dongan hills', 'egbertville', 'emerson hill', 'grant city', 'grasmere', 'midland beach', 'new dorp', 'new springville', 'oakwood', 'ocean breeze', 'old town', 'south beach', 'todt hill', 'travis', 'annadale', 'arden heights', 'bay terrace', 'charleston', 'eltingville', 'great kills', 'greenridge', 'huguenot', 'pleasant plains', 'prince’s bay', 'richmond valley', 'rossville', 'tottenville', 'woodrow', 'melrose', 'mott haven', 'port morris', 'hunts point', 'longwood', 'claremont', 'concourse village', 'crotona park', 'morrisania', 'concourse', 'high bridge', 'fordham', 'morris heights', 'mount hope', 'university heights', 'bathgate', 'belmont', 'east tremont', 'west farms', 'bedford park', 'norwood', 'university heights', 'fieldston', 'kingsbridge', 'kingsbridge heights', 'marble hill', 'riverdale', 'spuyten duyvil', 'van cortlandt village', 'bronx river', 'bruckner', 'castle hill', 'clason point', 'harding park', 'parkchester', 'soundview', 'unionport', 'city island', 'co-op city', 'locust point', 'pelham bay', 'silver beach', 'throgs neck', 'westchester square', 'allerton', 'bronxdale', 'laconia', 'morris park', 'pelham gardens', 'pelham parkway', 'van nest', 'baychester', 'edenwald', 'eastchester', 'fish bay', 'olinville', 'wakefield', 'williamsbridge', 'woodlawn']

startTime = datetime.datetime.now()

#takes out all punctuation, numbers and tricky non-ascii characters
def remove_punctuation(s):
    s=str(s)
    t = ''.join(l for l in s if l in string.ascii_letters)
    t = t.lower()
    return t
strippedgazetteer = []
for i in GAZETTEER:
    j = remove_punctuation(i)
    strippedgazetteer.append(i)

#Getting just the UserID column from my csv file that aggregates every
# csv of Search API results, generated by my readalltweets.py script. 
# This might not be the way to go--might be better to take the code
#  from that script and put it directly in here. 
allUserIDs = pd.read_csv('concat.csv', usecols = ['UserID'], error_bad_lines = 
    False, warn_bad_lines = True)
allUserIDs['location'] = np.zeros(len(allUserIDs['UserID']))

#Going through the file for each social landmark that contains just the
# UserIDs for their followers, storing that list in a dataframe, which 
# is stored within the list 'sociallandmarkFollowers'
numberOfSocialLandmarks = 0
socialLandmarkFollowers = []
socialLandmarkNames = []

for csvfile in glob.glob('sociallandmarks/*followerdetails.csv'):
    # IMPORTANT: Because there are new line characters in some of the location fields and
    # the latest edition of pandas doesn't like that, we have to FIRST open
    # the file in "universal new line mode", then read it with pandas read_csv
    csvfileUniv = open(csvfile, 'U')
    socialLandmarkHandle = csvfile[16:-19]
    print socialLandmarkHandle
    socialLandmarkNames.append(socialLandmarkHandle)
    df = pd.read_csv(csvfileUniv, usecols=['UserID', 'location'])
    #adding the social landmarks to a list of lists. The user ids for each 
    #social landmark is sorted so I can use binary search when creating
    #the matrix
    socialLandmarkFollowers.append([socialLandmarkHandle, sorted(df['UserID'].values)])
    #adding the user ids from the social landmark list to my master list of
    #user ids (including the user ids pulled from the twitter Search API)
    allUserIDs = allUserIDs.append(df)
    numberOfSocialLandmarks += 1

# print 'sorting social landmark followers list of lists'
sociallandmarkFollowers = sorted(socialLandmarkFollowers, key=lambda x: x[0])

# print "before dropping duplicates:"
# print allUserIDs.shape

print 'dropping duplicates from all user ids list'
allUserIDs = allUserIDs.drop_duplicates(['UserID'])

# print "after dropping duplicates"
# print allUserIDs.shape

print 'converting all user id dataframe to numpy arrays'
UserIDList = allUserIDs['UserID'].values
userlocations = allUserIDs['location'].values

# Going through here is each userID we have from the search API AND
# social landmark , checking
# if UserID is in any of the sociallandmark lists, looping 

# initializing the matrix with zeros, so that changes only have to be made
# if a match is found. Matrix has width = number of social landmarks + 1
# for 
numberOfUserIDs = len(UserIDList)
matrix = np.zeros((numberOfUserIDs, numberOfSocialLandmarks+1))

print "starting matrix loop"

for i in range(numberOfUserIDs):
    for j in strippedgazetteer:
        if j in remove_punctuation(userlocations[i]):
            matrix[i, numberOfSocialLandmarks] = 1
    #IMPORTANT to keep the social landmark count each time a userid is
    # queried -- that's how it's stored in the correct matrix cell
    socialLandmarkCount = 0
    for socialLandmark in socialLandmarkFollowers:
        if binary_search(socialLandmark[1], UserIDList[i]):
            matrix[i, socialLandmarkCount] = 1
        socialLandmarkCount +=1
    #social landmark count has to be reset each time a userid has been queried
    #through every one of the landmarks.
    socialLandmarkCount = 0

# I need to add on the isnewyorker flag to the sociallandmark names for the 
# matrix dataframe column headers.
socialLandmarkNames.append('isnewyorker')

dfmatrix = pd.DataFrame(data=matrix, index=UserIDList, columns=socialLandmarkNames)

dfmatrix.to_csv('mastermatrix.csv', index_label='UserID')

print dfmatrix.shape

endTime = datetime.datetime.now() - startTime

print "runtime:"
print endTime

#takes about 2h 40m, now that it's doing the searching within the gazetteer as well.