import pandas as pd
import os
import sys
import glob

totalNumGeo = 0
totalTweets = 0

for csvfile in glob.glob('cussac/*.csv'):
	df = pd.read_csv(csvfile)

	numGeo = df[(df["Geo"] != 'None')]["Tweeted_At"].count()
	numNotGeo = df[(df["Geo"] == 'None')]["Tweeted_At"].count()
	total = df["Tweeted_At"].count()

	print 'file: ' + csvfile
	print '\t len(df) - '+ str(len(df))
	# print '\t len(ids) - '+ str(len(ids))
	print '\t Geo enabled: ' + str (numGeo) + ' (' + str(numGeo*100.00/total) + '%)'
	print '\t Geo disabled: ' + str (numNotGeo) + ' (' + str(numNotGeo*100.00/total) + '%)'
	print '\t Total: ' + str(total)

	totalNumGeo = totalNumGeo + numGeo
	totalTweets = totalTweets + total
	
	print "totalNumGeo: " + str(totalNumGeo)
	print "totalTweets : " + str(totalTweets)
	print "overall avg: " + str(totalNumGeo*100.0/totalTweets) + '%'