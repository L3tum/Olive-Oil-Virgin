import time
from slackclient import SlackClient
import sys
sys.dont_write_bytecode = True
import glob
import yaml
import json
import logging

botToken = "xoxb-5134150563-itkh6B9inXzlkrCWaBdkCeLS"
itrID = "U053KLMS7"
channelRandom = "C050768H2"
output = []
Matrix = [[0 for x in range(5)] for x in range(5)]

#currently the max numbers of things in Matrix are 5, change that by changing above range(number)
MatrixLength = 5
bitteWendenId = "U0539QRF3"

sc = SlackClient(botToken)
if sc.rtm_connect():
    #adds the outputs
    Matrix[0][0] = "Hi"
    Matrix[0][1] = "Hello"

    #get Authentification
    dat = sc.api_call("api.test")
    dat2 = sc.api_call("auth.test", token = botToken)
    print dat
    print "--------"
    print dat2


    while True:
        sc.api_call("users.setPresence", token = botToken, presence = "away")

        for data in sc.rtm_read():
            if "type" in data:
               if data["type"] == "message":
                  chanel = data["channel"]
                  if "text" in data:
                     text = data["text"]
                     for x in range(0, MatrixLength):
                         if text == Matrix[x][0]:
                            sc.api_call("chat.postMessage", channel = chanel, text = "{} <@{}|{}>".format(Matrix[x][1], sc.server.users.find(data["user"]).id, sc.server.users.find(data["user"]).name, bitteWendenId), as_user = True, parse = True)

        time.sleep(1)
else:
    print "Connection Failed, invalid token?"