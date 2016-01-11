__author__ = 'chintanpanchamia'

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
import ConfigParser
import json
import random
import cpancha
import time

#config = ConfigParser.ConfigParser()
#config.read('.twitter')

#consumer_key = config.get('apikey', '')
#consumer_secret = config.get('apikey', '')
#access_token = config.get('token', '')
#ccess_token_secret = config.get('token', '')
#stream_rule = config.get('app', 'rule')
#account_screen_name = config.get('socialcomputingp2', '').lower()
#account_user_id = config.get('socialcomputingp2', '')




account_screen_name = 'chinpanz10'
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitterApi = API(auth)

class CallActionFeedback(StreamListener):
    #curr_loc = ''
    def feedback(self, action, rmode):
        if(cpancha.curr_loc is 'hunt'):
            if(rmode is 'silent'):
                if(action is 'yes' or 'Yes' or 'No' or 'No'):
                    return 'Neutral'
            else:
                return 'Negative'
        if(cpancha.curr_loc is 'eb2'):
            if(rmode is 'silent'):
                if(action is 'Yes' or 'yes' or 'No' or 'no'):
                    return 'Neutral'
            else:
                if(action is 'Yes' or 'yes'):
                    return 'Negative'
                else:
                    return 'Neutral'
        if(cpancha.curr_loc is 'carmichael'):
            return 'Neutral'
        if(cpancha.curr_loc is 'oval'):
            return 'Neutral'
        if(cpancha.curr_loc is 'party'):
            if(action is 'Yes' or 'yes'):
                return 'Neutral'
            else:
                return 'Positive'


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
        print tweetText1


        # if(tweetText1[0] == 'I' or tweetText1[0] == 'i'): #Handles my own check-in, and starts listening only if I check-in, and continues to listen there onward only when I stop
        #     if(tweetText1[5].split('_')[1] == 'cpancha'):
        #         print 'here'
        #         curr_loc = tweetText1[4]
        #         myMode = ''
        #         expectedMode = ''
        #         if(curr_loc == '#hunt'):
        #             myMode = random.choice(['Silent','Loud'])
        #             expectedMode = 'Silent'
        #         if(curr_loc == '#eb2'):
        #             myMode = random.choice(['Silent','Loud'])
        #             expectedMode = 'Silent'
        #         if(curr_loc == '#carmichael'):
        #             myMode = random.choice(['Silent','Loud'])
        #             expectedMode = 'Loud'
        #         if(curr_loc == '#oval'):
        #             myMode = random.choice(['Silent','Loud'])
        #             expectedMode = 'Loud'
        #         if(curr_loc == '#party'):
        #             myMode = random.choice(['Silent','Loud'])
        #             expectedMode = 'Loud'
        #         print myMode, expectedMode
        #
        # if(curr_loc is not '' and screenName != account_screen_name):
        #     if(tweetText1[4] == curr_loc):
        #         reply = '@' + screenName + '\n' + 'Name: ' + 'Chintan Panchamia' + '\n' + 'MY_MODE: ' + myMode + '\n' + 'EXPECTED_MODE: ' + expectedMode + '\n' + tweetText1[5] + ' ' + tweetText1[6]
        #         print reply
        #         twitterApi.update_status(status = reply)


        # if(tweetText1[0] == '@' + account_screen_name and 'Name:' in tweetText1[1]):
        #     with open('locationPref.json','a') as loc:
        #         loc.write(tweetText)
        #     if(float(cpancha.location_response_counter)/3 == 0):
        #         reply = 'CALL ' + tweetText1[4]
        #         twitterApi.update_status(status = reply, in_reply_to_status_id = tweetId)
        #         print "The Call has been requested"
        #     cpancha.location_response_counter + 1

        # if(tweetText1[0] == 'CALL' or 'Call' or 'call'):
        #     bot = random.choice(cpancha.my_bots.keys())
        #     urgency = 0;
        #     if(cpancha.my_bots[bot] == 'family' or 'colleague' or 'friend'):
        #         urgency = 1;
        #     else:
        #         urgency = 0;
        #
        #     reply = '@' + screenName + '\n' + 'Call from: ' + bot + '\n' + 'URGENCY: ' + str(urgency) + '\n' + tweetText1[1] + ' ' + tweetText1[2]
        #     print reply
        #     twitterApi.update_status(status = reply, in_reply_to_status_id = tweetId)

        if(tweetText1[0] == 'Action' or 'ACTION' and tweetText1[2].split('_')[1] in cpancha.neighbors):
            #insert code for extracting the neighbor and their ringer modes from incoming tweet
            neighborID = tweetText1[2].split('_')[1]
            rmode = cpancha.neighbors[neighborID]
            #emode = cpancha.neighbors[neighborID].split()[1]
            action = tweetText1[1]
            response = self.feedback(action, rmode)
            reply = '@' + screenName + '\n' + 'Name: Chintan Panchamia' + '\n' + 'RESPONSE: ' + response + '\n' + tweetText1[2] + ' ' + tweetText1[3]
            twitterApi.update_status(status = reply, in_reply_to_status_id = tweetId)
            time.sleep(5)




        # if(tweetText1[0] == '@' + account_screen_name and tweetText1[1] == 'Call' or 'call'):
        #     botname = tweetText1[3]
        #     action = random.choice(['Yes','No'])
        #     ##THIS IS WHERE THE UTILITY FUNCTION SHALL BE PLACED DURING THE 2nd PHASE OF P2
        #     ##IT WILL CONSIDER THE REQUIRED PARAMETERS AND DO PRODUCE THE IDEAL OUTPUT
        #     #action = utility()
        #     reply = 'ACTION: ' + action + ' ' + tweetText1[6] + ' ' + tweetText1[7]
        #     twitterApi.update_status(status=reply)
        return True




    def on_error(self, status):
        print status
        return True

if __name__ == '__main__':
    l = CallActionFeedback()
    stream = Stream(auth, l)
    stream.filter(track=['#P2CSC555F15'])
