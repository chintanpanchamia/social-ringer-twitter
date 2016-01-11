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


class IncomingCallRequestHandler(StreamListener):
    #curr_loc = ''
    def utilityStatic(self, location, urgency, noise, relation):
        action = ''
        if(location is 'hunt' or 'eb2'):
            if(relation is 'family'):
                action = 'Yes'
            if(relation is 'colleague'):
                if(noise is '2' or '3' or '4' or '5'):
                    action = 'Yes'
                else:
                    action = 'No'
            elif(relation is 'friend'):
                if(urgency is '1' and noise is '3' or '4' or '5'):
                    action = 'Yes'
                else:
                    action = 'No'
        if(location is 'oval'):
            if(relation is 'colleague' or 'family' or 'friend'):
                action = 'Yes'
            else:
                if(urgency is '1'):
                    action = 'Yes'
                else:
                    action = 'No'
        if(location is 'carmichael'):
            if(relation is 'family'):
                action = 'Yes'
            elif(relation is 'friend' or 'colleague'):
                if(urgency is '1'):
                    action = 'Yes'
                else:
                    action = 'No'
            else:
                action = 'No'
        if(location is 'party'):
            if(relation is 'family'):
                if(urgency == 1 or noise is '1' or '2' or '3'):
                    action = 'Yes'
                else:
                    action = 'No'
            else:
                action = 'No'

        if(action is 'Yes'):
            action = 1
        else:
            action = -1



        print action
        feedback = []

        if(location is 'hunt'):
            with open('HuntHistory.csv', 'rb') as huntcsv:
                csvreader = csv.reader(huntcsv)
            for row in csvreader:
                if(row[0] is urgency and row[1] is relation and row[2] is noise and row[3] is action):
                    feedback.append(row[4])
            for i in feedback:
                sum = sum + int(feedback[i])
            huntcsv.close()
            if(sum >= 0):
                return action
            else:
                return -1 * action

        if(location is 'eb2'):
            with open('Eb2History.csv', 'rb') as eb2csv:
                huntreader = csv.reader(eb2csv)
            for row in huntreader:
                if(row[0] is urgency and row[1] is relation and row[2] is noise and row[3] is action):
                    feedback.append(row[4])
            for i in feedback:
                sum = sum + int(feedback[i])
            eb2csv.close()
            if(sum >= 0):
                return action
            else:
                return -1 * action

        if(location is 'carmichael'):
            with open('CarmichaelHistory.csv', 'rb') as carmichaelcsv:
                carmichaelreader = csv.reader(carmichaelcsv)
            for row in carmichaelreader:
                if(row[0] is urgency and row[1] is relation and row[2] is noise and row[3] is action):
                    feedback.append(row[4])
            for i in feedback:
                sum = sum + int(feedback[i])
            carmichaelcsv.close()
            if(sum >= 0):
                return action
            else:
                return -1 * action

        if(location is 'oval'):
            with open('OvalHistory.csv', 'rb') as ovalcsv:
                ovalreader = csv.reader(ovalcsv)
            for row in ovalreader:
                if(row[0] is urgency and row[1] is relation and row[2] is noise and row[3] is action):
                    feedback.append(row[4])
            for i in feedback:
                sum = sum + int(feedback[i])
            ovalcsv.close()
            if(sum >= 0):
                return action
            else:
                return -1 * action

        if(location is 'party'):
            with open('PartyHistory.csv', 'rb') as partycsv:
                partyreader = csv.reader(partycsv)
            for row in partyreader:
                if(row[0] is urgency and row[1] is relation and row[2] is noise and row[3] is action):
                    feedback.append(row[4])
            for i in feedback:
                sum = sum + int(feedback[i])
            partycsv.close()
            if(sum >= 0):
                return action
            else:
                return -1 * action




    #def utilityHistory(self, action):

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


        if(tweetText1[0] == '@' + account_screen_name and tweetText1[1] == 'Call' or 'call'):
            botname = tweetText1[3]
            relation = cpancha.my_bots[botname]
            location = cpancha.curr_loc
            urgency = tweetText1[5]
            noise = int(random.choice(['1','2','3','4','5']))
            action = self.utilityStatic(location, urgency, noise, relation)

            if(action is -1):
                action = 'No'
            else:
                action = 'Yes'
            ##THIS IS WHERE THE UTILITY FUNCTION SHALL BE PLACED DURING THE 2nd PHASE OF P2
            ##IT WILL CONSIDER THE REQUIRED PARAMETERS AND DO PRODUCE THE IDEAL OUTPUT
            #action = utility()
            cpancha.history = urgency + ',' + relation + ',' + noise + ',' + action

            reply = 'ACTION: ' + action + ' ' + tweetText1[6] + ' ' + tweetText1[7]
            twitterApi.update_status(status=reply, in_reply_to_status_id = tweetId)
            time.sleep(5)

        return True




    def on_error(self, status):
        print status
        return True

if __name__ == '__main__':
    l = IncomingCallRequestHandler()
    stream = Stream(auth, l)
    stream.filter(track=['#P2CSC555F15'])
