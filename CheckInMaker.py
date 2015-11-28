__author__ = 'chintanpanchamia'
import random
# from tweepy.streaming import StreamListener
# from tweepy import OAuthHandler
# from tweepy import Stream
#
# access_token = "2206438826-TTfR3KNPQdKdo7HvlftIKE9Mdwc1xJwRCsIw3S5"
# access_token_secret = "BAC8yk38M9ItUqH8boGsxi0z1OF7W1mBa2k5K8Ci7a30c"
# consumer_key = "45opyWmnEdNNKqPJOQ3jJczXK"
# consumer_key_secret = "iFt2MDExEY2BuYKgWXObBk7CcRFOPijbv6iVaBTeFb8ZVx5R7d"
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

#consumer_key = config.get("apikey", "45opyWmnEdNNKqPJOQ3jJczXK")
#consumer_secret = config.get("apikey", "iFt2MDExEY2BuYKgWXObBk7CcRFOPijbv6iVaBTeFb8ZVx5R7d")
#access_token = config.get("token", "2206438826-TTfR3KNPQdKdo7HvlftIKE9Mdwc1xJwRCsIw3S5")
#ccess_token_secret = config.get("token", "BAC8yk38M9ItUqH8boGsxi0z1OF7W1mBa2k5K8Ci7a30c")
#stream_rule = config.get("app", "rule")
#account_screen_name = config.get("socialcomputingp2", "chinpanz10").lower()
#account_user_id = config.get("socialcomputingp2", "2206438826")




account_screen_name = "chinpanz10"
access_token = "2206438826-WhmCoFFcnCSRCBs5NahWh4Zp3RCkPgFmjsvlN4U"
access_token_secret = "UFZ67WwOreS8bKVtIPZYZ570djzPVp1k1ddFcRVduCjBl"
consumer_key = "hvPueLbHPaW8hS7nqjsNgxJEy"
consumer_secret = "NFJkdCPup9O3YpOd4t4dkE8qBr4a2I2KK6ARJTmJl4e7oIyc8G"

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