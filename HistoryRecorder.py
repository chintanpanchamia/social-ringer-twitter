__author__ = 'chintanpanchamia'

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
import ConfigParser
import json
import random
import cpancha
import csv
import time
#config = ConfigParser.ConfigParser()
#config.read('.twitter')






account_screen_name = 'chinpanz10'
access_token = 
access_token_secret = 
consumer_key = 
consumer_secret = 

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitterApi = API(auth)

class HistoryRecorder(StreamListener):
    def on_data(self, data):
        #print raw_data
        tweet = json.loads(data.strip())
        #print tweet
        #inc.write(tweet)

        tweetId = str(tweet.get('id_str'))
        screenName = tweet.get('user',{}).get('screen_name')
        print screenName
        tweetText = tweet.get('text')
        tweetText1 = tweetText.split('\n')
        print tweetText1













        if(tweetText1[0] is '@'+account_screen_name and 'RESPONSE' in tweetText1):
            feedback = tweetText1[2].split()[1]
            history = cpancha.history + ',' + feedback
            if(cpancha.curr_loc is 'hunt'):
                f1 = open('HuntHistory.csv', 'wb')
                huntwriter = csv.writer(f1)
                huntwriter.writerow([history])
                f1.close()
            if(cpancha.curr_loc is 'eb2'):
                f2 = open('Eb2History.csv', 'wb')
                eb2writer = csv.writer(f2)
                eb2writer.writerow([history])
                f2.close()
            if(cpancha.curr_loc is 'oval'):
                f3 = open('OvalHistory.csv', 'wb')
                ovalwriter = csv.writer(f3)
                ovalwriter.writerow([history])
                f3.close()
            if(cpancha.curr_loc is 'carmichael'):
                f4 = open('CarmichaelHistory.csv', 'wb')
                carmichaelwriter = csv.writer(f4)
                carmichaelwriter.writerow([history])
                f4.close()
            if(cpancha.curr_loc is 'party'):
                f5 = open('PartyHistory.csv', 'wb')
                partywriter = csv.writer(f5)
                partywriter.writerow([history])
                f5.close()

        time.sleep(5)




        return True

    def on_error(self, status_code):
        print status_code
        return True

if __name__ == '__main__':
    l = HistoryRecorder()
    stream = Stream(auth, l)
    stream.filter(track=['#P2CSC555F15'])

