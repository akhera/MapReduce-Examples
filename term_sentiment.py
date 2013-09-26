import sys
import urllib
import json
from collections import defaultdict

#def hw():
    #print 'Hello, world!'

#def lines(fp):
    #print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {}
    tweets={}
    words = []
    sentence = []
    new_words = defaultdict(int)

    
    
    for line in sent_file:
       term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
       scores[term] = int(score)  # Convert the score to an integer.
       
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
            if text in scores.keys():
                val+= scores[text]
            else:
                   new_words[text]+=val             
    
    for word,value in new_words.iteritems():
         print word,value
        
if __name__ == '__main__':
    main()
