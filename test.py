__author__ = 'chintanpanchamia'

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
import ConfigParser
import json
import random

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
access_token = '2206438826-TTfR3KNPQdKdo7HvlftIKE9Mdwc1xJwRCsIw3S5'
access_token_secret = 'BAC8yk38M9ItUqH8boGsxi0z1OF7W1mBa2k5K8Ci7a30c'
consumer_key = '45opyWmnEdNNKqPJOQ3jJczXK'
consumer_secret = 'iFt2MDExEY2BuYKgWXObBk7CcRFOPijbv6iVaBTeFb8ZVx5R7d'

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitterApi = API(auth)

#f1 = open('incoming.json', 'a')
#locations = {'#hunt','#eb2','#carmichael','#oval','#party'}
my_bots = {'Anakin':'family','Chewbacca':'friend','Han':'friend','Jango':'stranger','JarJar':'friend','Leia':'family','Luke':'family','Mace':'colleague','ObiWan':'colleague','Padme':'family','Yoda':'colleague'}
#curr_loc = '#hunt'
#loc_count = 0
neighbors = {}

class MyTwitterBot(StreamListener):
    #curr_loc = ''
    def on_data(self, data):
        print data
        #inc.write(data)

        tweet = json.loads(data.strip())
        #print tweet
        #inc.write(tweet)

        tweetId = str(tweet.get('id_str'))
        screenName = tweet.get('user',{}).get('screen_name')
        print screenName
        tweetText = tweet.get('text')
        tweetText1 = tweetText.split()
        print tweetText1


        if(tweetText1[0] == 'I' or tweetText1[0] == 'i'): #Handles my own check-in, and starts listening only if I check-in, and continues to listen there onward only when I stop
            if(tweetText1[5].split('_')[1] == 'cpancha'):
                print 'here'
                curr_loc = tweetText1[4]
                myMode = ''
                expectedMode = ''
                if(curr_loc == '#hunt'):
                    myMode = random.choice(['Silent','Loud'])
                    expectedMode = 'Silent'
                if(curr_loc == '#eb2'):
                    myMode = random.choice(['Silent','Loud'])
                    expectedMode = 'Silent'
                if(curr_loc == '#carmichael'):
                    myMode = random.choice(['Silent','Loud'])
                    expectedMode = 'Loud'
                if(curr_loc == '#oval'):
                    myMode = random.choice(['Silent','Loud'])
                    expectedMode = 'Loud'
                if(curr_loc == '#party'):
                    myMode = random.choice(['Silent','Loud'])
                    expectedMode = 'Loud'
                print myMode, expectedMode

        if(curr_loc is not '' and screenName != account_screen_name):
            if(tweetText1[4] == curr_loc):
                reply = '@' + screenName + '\n' + 'Name: ' + 'Chintan Panchamia' + '\n' + 'MY_MODE: ' + myMode + '\n' + 'EXPECTED_MODE: ' + expectedMode + '\n' + tweetText1[5] + ' ' + tweetText1[6]
                print reply
                twitterApi.update_status(status = reply)


        if(tweetText1[0] == '@' + account_screen_name and tweetText1[1] == 'Name:'):
            with open('locationModes.json','a') as loc:
                loc.write(tweet.get('text'))
            if(loc_count/3 == 0):
                reply = 'CALL ' + tweetText1[7] + ' ' + tweetText1[8]
                twitterApi.update_status(status=reply)
            loc_count + 1

        if(tweetText1[0] == 'CALL' or 'Call' or 'call'):
            bot = random.choice(my_bots.keys())
            urgency = 0;
            if(my_bots[bot] == 'family' or 'colleague' or 'friend'):
                urgency = 1;
            else:
                urgency = 0;

            reply = '@' + screenName + '\n' + 'Call from: ' + bot + '\n' + 'URGENCY: ' + str(urgency) + '\n' + tweetText1[1] + ' ' + tweetText1[2]
            twitterApi.update_status(status=reply)

        if(tweetText1[0] == '@' + account_screen_name and tweetText1[1] == 'Call' or 'call'):
            botname = tweetText1[3]
            action = random.choice(['Yes','No'])
            ##THIS IS WHERE THE UTILITY FUNCTION SHALL BE PLACED DURING THE 2nd PHASE OF P2
            ##IT WILL CONSIDER THE REQUIRED PARAMETERS AND DO PRODUCE THE IDEAL OUTPUT
            #
            reply = 'ACTION: ' + action + ' ' + tweetText1[6] + ' ' + tweetText1[7]
            twitterApi.update_status(status=reply)
        return True




    def on_error(self, status):
        print status
        return True

if __name__ == '__main__':
    l = MyTwitterBot()
    stream = Stream(auth, l)
    stream.filter(track=['#P2CSC555F15'])





