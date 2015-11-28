__author__ = 'chintanpanchamia'

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
import ConfigParser
import json
import random
import cpancha

#config = ConfigParser.ConfigParser()
#config.read('.twitter')

#consumer_key = config.get('apikey', '45opyWmnEdNNKqPJOQ3jJczXK')
#consumer_secret = config.get('apikey', 'iFt2MDExEY2BuYKgWXObBk7CcRFOPijbv6iVaBTeFb8ZVx5R7d')
#access_token = config.get('token', '2206438826-TTfR3KNPQdKdo7HvlftIKE9Mdwc1xJwRCsIw3S5')
#ccess_token_secret = config.get('token', 'BAC8yk38M9ItUqH8boGsxi0z1OF7W1mBa2k5K8Ci7a30c')
#stream_rule = config.get('app', 'rule')
#account_screen_name = config.get('socialcomputingp2', 'chinpanz10').lower()
#account_user_id = config.get('socialcomputingp2', '2206438826')




account_screen_name = 'chinpanz10'
access_token = "2206438826-WhmCoFFcnCSRCBs5NahWh4Zp3RCkPgFmjsvlN4U"
access_token_secret = "UFZ67WwOreS8bKVtIPZYZ570djzPVp1k1ddFcRVduCjBl"
consumer_key = "hvPueLbHPaW8hS7nqjsNgxJEy"
consumer_secret = "NFJkdCPup9O3YpOd4t4dkE8qBr4a2I2KK6ARJTmJl4e7oIyc8G"

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitterApi = API(auth)



class MyTwitterBot(StreamListener):

    def on_data(self, data):

        #print data
        #inc.write(data)

        tweet = json.loads(data.strip())
        #print tweet
        #inc.write(tweet)

        tweetId = str(tweet.get('id_str'))
        screenName = tweet.get('user',{}).get('screen_name')
        print screenName
        tweetText = tweet.get('text')
        tweetText1 = tweetText.split()
        print tweetText


        if(tweetText1[0] == 'I' or tweetText1[0] == 'i'): #Handles my own check-in, and starts listening only if I check-in, and continues to listen there onward only when I stop
            if(tweetText1[5].split('_')[1] == 'cpancha'):
                if(cpancha.curr_loc == tweetText1[4].split('#')[1]):
                    return True
                else:
                    #print 'here'
                    cpancha.curr_loc = tweetText1[4].split('#')[1]
                    #myMode = ''
                    #expectedMode = ''
                    if(cpancha.curr_loc == 'hunt'):
                        cpancha.myMode = random.choice(['Silent','Loud'])
                        cpancha.expectedMode = 'Silent'
                    if(cpancha.curr_loc == 'eb2'):
                        cpancha.myMode = random.choice(['Silent','Loud'])
                        cpancha.expectedMode = 'Silent'
                    if(cpancha.curr_loc == 'carmichael'):
                        cpancha.myMode = random.choice(['Silent','Loud'])
                        cpancha.expectedMode = 'Loud'
                    if(cpancha.curr_loc == 'oval'):
                        cpancha.myMode = random.choice(['Silent','Loud'])
                        cpancha.expectedMode = 'Loud'
                    if(cpancha.curr_loc == 'party'):
                        cpancha.myMode = random.choice(['Silent','Loud'])
                        cpancha.expectedMode = 'Loud'
                    print cpancha.myMode, cpancha.expectedMode
                    cpancha.neighbors = {}
                    cpancha.call_no = 1
                    cpancha.location_response_counter = 0
                    return True

            if(cpancha.curr_loc != "" and screenName != account_screen_name):
                if(tweetText1[4].split('#')[1] == cpancha.curr_loc):
                    #cpancha.neighbors.append(tweetText1[5])
                    cpancha.neighbors[tweetText1[5].split('_')[1]] = ''
                    reply = '@' + screenName + '\n' + 'Name: ' + 'Chintan Panchamia' + '\n' + 'MY_MODE: ' + cpancha.myMode + '\n' + 'EXPECTED_MODE: ' + cpancha.expectedMode + '\n' + tweetText1[5] + ' ' + tweetText1[6]
                    print reply
                    twitterApi.update_status(status = reply, in_reply_to_status_id = tweetId)
        return True







    def on_error(self, status):
        print status
        return True

if __name__ == '__main__':
    l = MyTwitterBot()
    stream = Stream(auth, l)
    stream.filter(track=['#P2CSC555F15'])
