# example of url : oauth_req( 'https://api.twitter.com/1.1/followers/ids.json?cursor=-1&screen_name=nypost&count=5000')

import sys
import os
import pandas as pd
import oauth2 as oauth
import json
import time
import datetime

#RAVI's credentials, for now.

CONSUMER_KEY='WCt81NXnk4R7QI9BNtBFWesNH'
CONSUMER_SECRET='xzVet8D3XWSB9vbc5hNpRpKfhBKIMoVTSlqrrWrIL9NIAaOz2v'
ACCESS_TOKEN='2874045741-asyKKDeBi1UB7wVS4RQWjBHMnkaQx2MKSePSGwx'
ACCESS_TOKEN_SECRET='Og2PiZpvnK5FqhQgTPKZKTr0WCYY1Z0tyOA1BvXOWOVG0'


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

def getAllFollowers(username):
	apicallcount = 0
	numberofrecords = 0
	baseApiUrl = 'https://api.twitter.com/1.1/followers/ids.json?screen_name=' + username + '&count=5000'
	cursor = -1
	data = {'UserID' : []}
	df = pd.DataFrame(data)
#checks to see if there's already a file with followers for this user -- if not, creates new csv file
	if not os.path.isfile('sociallandmarks/'+ username + 'followerids.csv'):
		df.to_csv('sociallandmarks/'+ username + 'followerids.csv')

	while cursor !='0':
		try:
			requestUrl = baseApiUrl + '&cursor=' + str(cursor)
			queryResults = oauth_req(requestUrl)
			# print queryResults
			actualCursor = queryResults['next_cursor_str']
			cursor = actualCursor
#creates dataframe. TODO: look into editing index start point (not critical)
			data = {'UserID' : queryResults['ids']}
			tempdf = pd.DataFrame(data)
# append to csv
			with open('sociallandmarks/'+ username + 'followerids.csv', 'a') as f:
				tempdf.to_csv(f, header=False)
#debugging/status update printing
			print datetime.datetime.now()
			apicallcount +=1
			print "number of API calls:" + str(apicallcount)
			numberofrecords = numberofrecords + len(queryResults['ids'])
			print 'number of records:' +  str(numberofrecords) 
#debugging: making sure the cursor is changing, save most recent cursor in case script breaks before completing
			print 'latest cursor:' + cursor
			print 'sleeping now'
# sleeping one additional second than strictly necessary, just for kicks/to be safe.
			time.sleep(60)

		except:
			print 'Exceeded call limit, sleeping for 15 minutes'
			print datetime.datetime.now()
			print 'latest cursor:' + cursor
			time.sleep(900)
			continue

def main():
	if len(sys.argv) != 2:
		print 'please specify a username'
	username = sys.argv[1]
	# intiate call to fetch all followers for that username
	getAllFollowers(username)


if __name__ == '__main__':
	main()



