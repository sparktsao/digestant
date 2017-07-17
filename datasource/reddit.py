import sys
import traceback
import string
import multiprocessing as mp
import glob
import os
import requests
import requests.auth
import praw        
import pandas

def showtime(x):    
    import datetime
    return datetime.datetime.fromtimestamp(x).strftime('%Y-%m-%d')
        
class datahelper:
    
    def __init__(self):
        # get config from env
        self.reddit = praw.Reddit(client_id=os.environ['REDDIT_client_id'],
        client_secret=os.environ['REDDIT_client_secret'],
        password=os.environ['REDDIT_password'],
        user_agent=os.environ['REDDIT_user_agent'],
        username=os.environ['REDDIT_username'])
    def channelhot(self):
        subreddit = reddit.subreddit(channel)
        count = 0
        datar = []
        for submission in subreddit.hot(limit=None):
            print("Title: ", submission.title)
            print("---------------------------------\n")
            count+=1 
            datar.append(submission)
        return datar
        
    def getdata(self,querystring='deeplearning',channel='MachineLearning'):
            
        datar2 = []    
        result = self.reddit.subreddit(channel).search(querystring) 
        for r in result:
            datar2.append(r)
        f1 = pandas.DataFrame({"raw":datar2})
        f1["title"] = f1.raw.map(lambda x:x.title)
        f1["created"] = f1.raw.map(lambda x:showtime(x.created))
        f1["auther"] = f1.raw.map(lambda x:x.author.name)
        return f1
 

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print ('Usage: python '+sys.argv[0]+' <querystring>')
        sys.exit(1)
    
    ex = datahelper()
    print (ex.getdata(sys.argv[1]))
