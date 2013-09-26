import sys
import urllib
import json
from collections import defaultdict


def main():
    
    tweet_file = open(sys.argv[1])
    frequencies = defaultdict(int)
    tweets={}
    words = []
    sentence = []
    total_words = 0
    

    
    
          
    for line in tweet_file:
        tweets = json.loads(line ,'utf=8')
        if "text" in tweets:
               sentence.append(tweets["text"])

    for tweet in sentence:
        words.append(tweet.split())

       
    for tweet in words:
         val = 0
         for i,phrase in enumerate(tweet):
            text = phrase.encode('utf-8')
            frequencies[text]+=1
            
    for value in frequencies.values():
        total_words+=value
    #print total_words

    for key,value in frequencies.iteritems():
         print key, value/float(total_words)
        
if __name__ == '__main__':
    main()
