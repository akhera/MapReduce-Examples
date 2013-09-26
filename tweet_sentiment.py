import sys
import urllib
import json

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
    val = None
    
    
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
            if i == (len(tweet)- 1):
                print val

  

            
                              
                              
                                 



      #print scores.items() # Print every (term, score) pair in the dictionary

#response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft")
#pyresponse = json.load(response)
#results = pyresponse['results']

#for i in range(10):
 #print results[i]["text"]




    #hw()
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
