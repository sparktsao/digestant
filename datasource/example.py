import sys
import traceback
import string
import multiprocessing as mp
import glob
import os

class datahelper:
    
    def __init__(self):
        # get config from env
    
    def getdata(self,querystring):
        return None

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print 'Usage: python '+sys.argv[0]+' <querystring>'
        sys.exit(1)
    
    ex = datahelper()
    print ex.getdata(sys.argv[1])

