import sys
import traceback
import string
import multiprocessing as mp
import glob
import os

class datahelper:
    
    def __init__(self):
        # get config from env
        a = 1 
    
    def getdata(self,querystring):
        import twitter
        import reddit
        import pandas
        o1 = twitter.datahelper()
        o2 = reddit.datahelper()
        f1 = o1.getdata("123")
        f2 = o2.getdata("deep")
        f1["tag"] = "twitter"
        f2["tag"] = "reddit"
        f3 = pandas.concat([f1,f2],axis=0,ignore_index=True)
        return f3

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print ('Usage: python '+sys.argv[0]+' <querystring>')
        sys.exit(1)
    
    ex = datahelper()
    print (ex.getdata(sys.argv[1]))

