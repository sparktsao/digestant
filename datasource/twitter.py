import sys
import os
import json
import time
import pprint
import pickle
import tweepy

from collections import defaultdict
class datahelper:
    
    def __init__(self):
        # get config from env
        self.pp = pprint.PrettyPrinter(indent=4)
        # Consumer keys and access tokens, used for OAuth
        consumer_key = os.environ['TWITTER_consumer_key']         
        consumer_secret = os.environ['TWITTER_consumer_secret']
        access_token = os.environ['TWITTER_access_token']
        access_token_secret = os.environ['TWITTER_token_secret']
        # OAuth process, using the keys and tokens

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        self.api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True) 
    
    def getdata(self,querystring):
        tweets = self.api.user_timeline(screen_name='StopMalvertisin',count=300)
        date_arr, twarr,raw = [],[],[]
        result = []
        for tw in tweets:
            result.append("%s\t%s"%(tw.created_at.strftime('%Y-%m-%d %H-%M'),tw.text))
            date_arr.append(tw.created_at.strftime('%Y-%m-%d %H-%M'))
            twarr.append(tw.text)
            raw.append(tw)
        import pandas
        f1 = pandas.DataFrame({"created":date_arr,"title":twarr,"raw":raw})
        f1["auther"] = 'StopMalvertisin'
        return f1

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print ('Usage: python '+sys.argv[0]+' <querystring>')
        sys.exit(1)
    
    ex = datahelper()
    print (ex.getdata(sys.argv[1]))
