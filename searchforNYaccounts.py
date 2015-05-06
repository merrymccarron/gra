import sys
import os
import pandas as pd
import oauth2 as oauth
import json
import time
import datetime
import string

CONSUMER_KEY='FqjFRT1OHl6xyIGoq9uXSA'
CONSUMER_SECRET='KuhoVREmf7ngwjOse2JOLJOVXNCi2IVEzQZu2B8'
ACCESS_TOKEN='114454541-xcjy2sbl7Rr4oIaogsaBrlVL5H4CvcdvOSMy3MnR'
ACCESS_TOKEN_SECRET='yyBBOJhxgfw9pezZda2hWF94doONSd50y0JoylYjL3rmY'


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


# URL = 'https://api.twitter.com/1.1/users/search.json?q=New+York+City&page='+ pagecount +'&count=20'

def get_nyc_accounts(searchterm):
    data = {'UserID' : [], 'location' : [], 'screen_name' : [], 'name': [], 'geo_enabled': [], 
        'followers_count':[], 'verified':[], 'time_zone': [], 'geo': [], 'statuses_count': [],
        'description': []}
    df = pd.DataFrame(data)
    if not os.path.isfile(searchterm + 'Searchuserdetails.csv'):
        df.to_csv(searchterm + 'Searchuserdetails.csv', header = True, columns = ['UserID', 
            'location', 'screen_name', 'name', 'geo_enabled', 'followers_count', 'verified', 
            'time_zone', 'geo', 'statuses_count', 'description'], engine='python')

    for i in range(50):
        #this api is limited to the first 1000 results
        URL = 'https://api.twitter.com/1.1/users/search.json?q=' + searchterm + '&page='+ 
            str(i) +'&count=20'
        try:
            data = oauth_req(URL)
        except:
            print "error after " + str(i) + "calls, exiting program at:"
            # print 'sleeping 1 minute'
            # time.sleep(60)
            print time.time.now()
            break
        else:
            tempdf = pd.DataFrame(data=data)
            with open(searchterm + 'Searchuserdetails.csv', 'a') as f:
                    tempdf['name'] = tempdf['name'].apply(lambda x: x.encode('ascii', 'ignore'))
                    tempdf['location'] = tempdf['location'].apply(lambda x: x.encode('ascii', 'ignore'))
                    tempdf['description'] = tempdf['description'].apply(lambda x: x.encode('ascii', 'ignore'))
                    tempdf.to_csv(f, header=False, columns = ['id_str', 'location', 'screen_name', 
                        'name', 'geo_enabled', 'followers_count', 'verified', 'time_zone', 'geo', 
                        'statuses_count', 'description'], engine='python')#, encoding = 'utf-8')
            
            print "number of API calls:" + str(i)
            print 'sleeping now'
            time.sleep(5)


def main():
    # if len(sys.argv) != 2:
    #     print 'please specify a search term'
    # username = sys.argv[1]
    searchterm = sys.argv[1]
    get_nyc_accounts(searchterm)

if __name__ == '__main__':
    main()

