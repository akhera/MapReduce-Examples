import sys
import urllib
import json
import operator

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
    tweet_scores = []
    states = {}
    index = 0
    
    
    for line in sent_file:
       term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
       scores[term] = int(score)  # Convert the score to an integer.
       
    for line in tweet_file:
        tweets = json.loads(line ,'utf=8')
        if "text" in tweets and "place" in tweets and tweets["place"] is not None and tweets["place"]["country_code"] == "US":
               sentence.append(tweets["text"])
               states[tweets["place"]["full_name"][-2:].encode('utf-8')] = 0
    

    for tweet in sentence:
        words.append(tweet.split())

       
    for tweet in words:
        val = 0
        for i,phrase in enumerate(tweet):
            text = phrase.encode('utf-8')
            if text in scores.keys():
                 val+=scores[text]
            if i == (len(tweet)-1):
                tweet_scores.append(val)
    
    
    index = 0
    for key,val in states.iteritems():
        states[key] += tweet_scores[index]
        index+=1
    
    print max(states, key=states.get)
        


if __name__ == '__main__':
    main()
