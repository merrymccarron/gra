# example URL : https://api.twitter.com/1.1/search/tweets.json?q=&geocode=-22.912214,-43.230182,1km

import sys
import os
import pandas as pd
import oauth2 as oauth
import json
import time
import datetime

#these are my credentials, not the CUSP ones we've been using on other API calls.

CONSUMER_KEY='UuEin53ZlFMxUHHVmbRu1iwrF'
CONSUMER_SECRET='BDfZeD0aXeaTrnH77ESzJpKm9mNAGaZmukOTTGLjALdDHltVR8'
ACCESS_TOKEN='27922176-yH551pDKiaHwYesntTewcDghGmMXuaitiQdNRKUyx'
ACCESS_TOKEN_SECRET='zha0VzXiO9xxMLzIUxSd01CGtyKGcmS3S6BPcSkwBBTNm'


def oauth_req(url, http_method="GET", post_body='', http_headers=None):
	consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
	token = oauth.Token(key=ACCESS_TOKEN, secret=ACCESS_TOKEN_SECRET)
	client = oauth.Client(consumer, token)
	resp, content = client.request( url, method=http_method, body=post_body, headers=http_headers)
	content = json.loads(content)
	if resp['status'] != '200':
		raise Exception("Invalid response %s." % resp['status'])
		# TODO: consider terminating the script if theres an error
	return content

def getTweets():
	apicallcount = 0
	numberofrecords = 0
	numRecordsSinceWrite = 0
	baseurl = "https://api.twitter.com/1.1/search/tweets.json?q=&geocode=40.69,-73.94,20mi"
	# data = {'Tweet ID': [], 'Tweeted_At': [], 'Profile_Created_at': [], 'Username': [], 'UserID' : [], 'location' : [], 'Enabled': [], 'Place': [], 'Geo': [], 'Text': [], 'Retweeted_Count': []}
	# df = pd.DataFrame(data)
	# filetime = time.time()
	# if not os.path.isfile('gothamistfollowerdetails.csv'):
	# 	df.to_csv('gothamistfollowerdetails.csv')
	while True:
		if numRecordsSinceWrite >= 3000:
			tempdf.to_csv('tweets_' + now + '.csv', header=True, columns = ['id_str', 'etcetc'])
		else:
			try:
				now = time.time()
				queryResults = oauth_req(baseurl)
				data = queryResults
				tempdf = pd.DataFrame(data=data)
				numRecordsSinceWrite = #get number of records in the tempdf?
			

#debugging script
			# df = pd.DataFrame(data = data)

		except:
			print 'Exceeded call limit, sleeping for 15 minutes'
			print datetime.datetime.now()
			time.sleep(901)
			continue








'''
--------- pseudocode ------
-- get now ""
-- check number of records
-- if number of records >= 2500: save to csv
	- need to be storing these tweets in memory some how...
	- name csv according to now
	- need to then clear out the DF 
-- sleep for 5 seconds
'''