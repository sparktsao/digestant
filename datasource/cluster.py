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

    def clusterlabel(self,clusterresult,summary):
        cid = len(summary)%2
        desc = summary[0:20]
        return (cid,desc)

    def cluster(self,dfx):

        clusterresult = None
        dfx["cid"] = dfx.title.map(lambda x:self.clusterlabel(clusterresult,x)[0])
        dfx["c_desc"] = dfx.title.map(lambda x:self.clusterlabel(clusterresult,x)[1])
        return dfx

    def getdata(self,querystring):
        import pandas
        import agg1
        o1 = agg1.datahelper()
        df1 = o1.getdata(querystring)
        df1 = self.cluster(df1)
        return df1

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print ('Usage: python '+sys.argv[0]+' <querystring>')
        sys.exit(1)
    
    ex = datahelper()
    print (ex.getdata(sys.argv[1]))

