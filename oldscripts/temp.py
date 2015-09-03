#TODO: make the script dynamic for follower ID.

import sys
import os
import pandas as pd
import oauth2 as oauth
import json
import time
import datetime
import itertools as it
import string

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
    # print resp['status']
    return content

def followers_slice(listofFollowers, apicallcount):
    start = apicallcount * 100
    end = start + 99
    useridSlice = it.islice(listofFollowers, start, end)
    useridSliceCommaSep = ','.join(map(str,useridSlice))
    return useridSliceCommaSep


def get_follower_details():
    followersDF = pd.read_csv('sociallandmarks/nyuniversityfollowerids.csv')
    listofFollowers = followersDF['UserID'].tolist()
    numberOfFollowers = len(listofFollowers)
    apicallcount = 0
    endOfCurrSlice = apicallcount * 100 + 99
    baseApiUrl = 'https://api.twitter.com/1.1/users/lookup.json?user_id=' 
    data = {'UserID' : [], 'location' : [], 'screen_name' : [], 'name': [], 'geo_enabled': []}
    df = pd.DataFrame(data)
#checks to see if there's already a file with followers for this user -- if not, creates new csv file
    if not os.path.isfile('sociallandmarks/nyuniversityfollowerdetails.csv'):
        df.to_csv('sociallandmarks/nyuniversityfollowerdetails.csv', header = True, columns = ['UserID', 'location', 'screen_name', 'name', 'geo_enabled'], engine='python')

    while endOfCurrSlice < numberOfFollowers:
        try:
            useridlistSlice = followers_slice(listofFollowers, apicallcount)
            requestUrl = baseApiUrl + useridlistSlice
            queryResults = oauth_req(requestUrl)
            data = queryResults
            tempdf = pd.DataFrame(data=data)
            with open('sociallandmarks/nyuniversityfollowerdetails.csv', 'a') as f:
                tempdf['name'] = tempdf['name'].apply(lambda x: x.encode('ascii', 'ignore'))
                tempdf['location'] = tempdf['location'].apply(lambda x: x.encode('ascii', 'ignore'))
                tempdf.to_csv(f, header=False, columns = ['id_str', 'location', 'screen_name', 'name', 'geo_enabled'], engine='python')#, encoding = 'utf-8')
#debugging script
            print datetime.datetime.now()
            apicallcount +=1
            endOfCurrSlice = apicallcount * 100 + 99
            print "number of API calls:" + str(apicallcount)
            print 'sleeping now'
            time.sleep(4.5)

        except:
            print 'Exceeded call limit, sleeping for 15 minutes'
            print datetime.datetime.now()
            time.sleep(900)
            continue



def main():
    # if len(sys.argv) != 2:
    #     print 'please specify a username'
    # username = sys.argv[1]
    get_follower_details()

if __name__ == '__main__':
    main()
