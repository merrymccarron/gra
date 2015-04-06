# -*- coding: utf-8 -*-
import sys
import os
import pandas as pd
import glob
import datetime

starttime = datetime.datetime.now()

gazetteer = ['gotham', 'new york', "NY,NY", 'ny', 'new york city', 'nyc', 'n.y.c.', 'brooklyn', 'bkln', 'bronx', 'staten island', 'si', 's.i.', 'queens', 'manhattan', 'greenpoint', 'williamsburg', 'boerum hill', 'brooklyn heights', 'brooklyn navy yard', 'clinton hill', 'dumbo', 'fort greene', 'vinegar hill', 'bedford-stuyvesant', 'bed stuy', 'bed-stuy', 'stuyvesant heights', 'bushwick', 'cypress hills', 'east new york', 'highland park', 'new lots', 'carroll gardens', 'cobble hill', 'gowanus', 'park slope', 'south slope', 'red hook', 'greenwood heights', 'sunset park', 'windsor terrace', 'crown heights', 'prospect heights', 'lefferts gardens', 'bay ridge', 'dyker heights', 'fort hamilton', 'bensonhurst', 'gravesend', 'borough park', 'kensington', 'midwood', 'brighton beach', 'coney island', 'flatbush', 'sheepshead bay', 'brownsville', 'east flatbush', 'bergen beach', 'canarsie', 'battery park city', 'financial district', 'tribeca', 'chinatown', 'greenwich village', 'little italy', 'lower east side', 'noho', 'soho', 'west village', 'alphabet city', 'chinatown', 'east village', 'two bridges', 'chelsea', 'clinton', 'hell\'s kitchen', 'hells kitchen', 'midtown', 'gramercy park', 'grammercy', 'kips bay', 'murray hill', 'peter cooper village', 'stuyvesant town', 'stuy town', 'sutton place', 'tudor city', 'turtle bay', 'waterside plaza', 'upper west side', 'lenox hill', 'roosevelt island', 'upper east side', 'yorkville', 'hamilton heights', 'manhattanville', 'morningside heights', 'harlem', 'east harlem', 'spanish harlem', 'randall’s island', 'inwood', 'washington heights', 'astoria', 'ditmars', 'garden bay', 'long island city', 'queensbridge', 'ravenswood', 'steinway', 'woodside', 'sunnyside', 'hunters point', 'elmhurst', 'jackson heights', 'corona', 'roosevelt avenue', 'fresh pond', 'glendale', 'maspeth', 'middle village', 'liberty park', 'ridgewood', 'forest hills', 'rego park', 'bay terrace', 'beechhurst', 'college point', 'flushing', 'linden hill', 'malba', 'queensboro hill', 'whitestone', 'willets point', 'briarwood', 'cunningham heights', 'flushing', 'fresh meadows', 'hilltop village', 'holliswood', 'jamaica estates', 'kew gardens hills', 'pomonok houses', 'utopia', 'kew gardens', 'ozone park', 'richmond hill', 'woodhaven', 'howard beach', 'lindenwood', 'tudor village', 'auburndale', 'bayside', 'douglaston', 'east flushing', 'hollis hills', 'little neck', 'oakland gardens', 'baisley park', 'jamaica', 'hollis', 'rochdale village', 'st. albans', 'springfield gardens', 'bellerose', 'brookville', 'cambria heights', 'floral park', 'glen oaks', 'laurelton', 'meadowmere', 'new hyde park', 'queens village', 'rosedale', 'arverne', 'bayswater', 'belle harbor', 'breezy point', 'edgemere', 'far rockaway', 'neponsit', 'rockaway park', 'arlington', 'castleton corners', 'clifton', 'concord', 'elm park', 'fort wadsworth', 'graniteville', 'grymes hill', 'livingston', 'mariners harbor', 'meiers corners', 'new brighton', 'port ivory', 'port richmond', 'randall manor', 'rosebank', 'st. george', 'shore acres', 'silver lake', 'stapleton', 'tompkinsville', 'west brighton', 'westerleigh', 'arrochar', 'bloomfield', 'bulls heads', 'dongan hills', 'egbertville', 'emerson hill', 'grant city', 'grasmere', 'midland beach', 'new dorp', 'new springville', 'oakwood', 'ocean breeze', 'old town', 'south beach', 'todt hill', 'travis', 'annadale', 'arden heights', 'bay terrace', 'charleston', 'eltingville', 'great kills', 'greenridge', 'huguenot', 'pleasant plains', 'prince’s bay', 'richmond valley', 'rossville', 'tottenville', 'woodrow', 'melrose', 'mott haven', 'port morris', 'hunts point', 'longwood', 'claremont', 'concourse village', 'crotona park', 'morrisania', 'concourse', 'high bridge', 'fordham', 'morris heights', 'mount hope', 'university heights', 'bathgate', 'belmont', 'east tremont', 'west farms', 'bedford park', 'norwood', 'university heights', 'fieldston', 'kingsbridge', 'kingsbridge heights', 'marble hill', 'riverdale', 'spuyten duyvil', 'van cortlandt village', 'bronx river', 'bruckner', 'castle hill', 'clason point', 'harding park', 'parkchester', 'soundview', 'unionport', 'city island', 'co-op city', 'locust point', 'pelham bay', 'silver beach', 'throgs neck', 'westchester square', 'allerton', 'bronxdale', 'laconia', 'morris park', 'pelham gardens', 'pelham parkway', 'van nest', 'baychester', 'edenwald', 'eastchester', 'fish bay', 'olinville', 'wakefield', 'williamsbridge', 'woodlawn']

punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
def remove_punctuation(s):
    s_sans_punct = ""
    for letter in s:
        if letter not in punctuation:
            s_sans_punct += letter
    s_sans_punct = s_sans_punct.replace(' ', '')
    return s_sans_punct

strippedgazetteer = []
for i in gazetteer:
    j = remove_punctuation(i)
    strippedgazetteer.append(j)

df = pd.DataFrame(data={'UserID':[], 'location': [],'screen_name': [], 'name':[], 
    'geo_enabled': []})

# df = pd.DataFrame(data=None)

for csvfile in glob.glob('sociallandmarks/*details.csv'):
    try:
        tempdf = pd.read_csv(csvfile, usecols=['UserID', 'location', 'screen_name', 
            'name', 'geo_enabled'], error_bad_lines = False, warn_bad_lines = True).fillna(
            value='None')
        df = df.append(tempdf)
        print csvfile
    except:
        print "could not read" + csvfile
        continue

print "dataframe before removing duplicates:" 
print df.shape

df = df.drop_duplicates(['UserID'])

UserIDsformatching = df['UserID'].values
locationsformatching = df['location'].values

numberOfUsersLocations = 0
numberOfNewYorkers = 0
UserIdsforNewYorkerMatrix = []
newYorkerYesNoforMatrix = []

ix = 0
for i in df['location']:
    UserIdsforNewYorkerMatrix.append(UserIDsformatching[ix])
    newYorkerYesNoforMatrix.append(0)
    # print UserIDsformatching[ix]
    if i != 'None':
        numberOfUsersLocations +=1
        j = remove_punctuation(i).lower()
        for k in strippedgazetteer:
            if k in j:
                numberOfNewYorkers +=1
                newYorkerYesNoforMatrix[ix]=1
                continue
    #         else:
    #             newYorkerYesNoforMatrix.append(0)
    # else:
    #     newYorkerYesNoforMatrix.append(0)
    ix += 1

print 'numberOfNewYorkers:' + str(numberOfNewYorkers)
print 'numberOfUsersLocations:' + str(numberOfUsersLocations)
print df.shape
# print df.head(10)

# df = pd.DataFrame(data={'UserID': [], 'NewYorker': []})

newYorkerUserIDmatrix = pd.DataFrame(data={'UserID': UserIdsforNewYorkerMatrix, 'newYorker': newYorkerYesNoforMatrix})
# print "newYorkerMatrix head"
# print newYorkerUserIDmatrix.head(10)

df['newyork']=newYorkerYesNoforMatrix

df.to_csv('sociallandmarks/slfollowersNYbyLocationText.csv')

newYorkerUserIDmatrix.to_csv('newyorkeryesnomatrix.csv')

elapsedtime = datetime.datetime.now() - starttime
print elapsedtime

'''# numberOfNewYorkers: 1,363,424
# numberOfUsersLocations: 3,734,594
# dataframe size: (6,726,888 rows, 6 columns)
# 12,621,391 rows before removing duplicates
'''
