import sys
import urllib
import json
from collections import defaultdict
import operator


def main():
    
    tweet_file = open(sys.argv[1])
    tweets={}
  
    hashtags = defaultdict(int)
    
    

    
    
          
    for line in tweet_file:
        tweets = json.loads(line ,'utf=8')
        if "entities" in tweets and len(tweets["entities"]["hashtags"]) > 0:
          hashtags[tweets["entities"]["hashtags"][0]["text"].encode("utf-8")] +=1

    sorted_hashtags = sorted(hashtags.iteritems(), key=operator.itemgetter(1))

    for tup,val in reversed(sorted_hashtags[:10]):
            print tup, float(val)
          

        
if __name__ == '__main__':
    main()
