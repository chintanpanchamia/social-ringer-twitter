__author__ = 'chintanpanchamia'
import random
# from tweepy.streaming import StreamListener
# from tweepy import OAuthHandler
# from tweepy import Stream
#
# 
#


# my_bots = {"Anakin":"family","Chewbacca":"friend","Han":"friend","Jango":"stranger","JarJar":"friend","Leia":"family","Luke":"family","Mace":"colleague","ObiWan":"colleague","Padme":"family","Yoda":"colleague"}
#
#
# bot = random.choice(my_bots.keys())
#
# print bot
#
# print my_bots[bot]


from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
import ConfigParser
import json
import random
import cpancha
import time
import os
import sys
#config = ConfigParser.ConfigParser()
#config.read(".twitter")






account_screen_name = "chinpanz10"
access_token = 
access_token_secret = 
consumer_key = 
consumer_secret = 

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitterApi = API(auth)
location = random.choice(cpancha.locations)

reply = 'I checked in at ' + '#' + location + ' #id_cpancha_' + str(cpancha.checkin) + ' #P2CSC555F15'
cpancha.checkin = cpancha.checkin + 1
cpancha.curr_loc = location
twitterApi.update_status(status=reply)
time.sleep(900)
execfile('CheckInMaker.py')
