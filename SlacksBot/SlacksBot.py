import time
from slackclient import SlackClient
import sys
sys.dont_write_bytecode = True
import glob
import yaml
import json
import logging

myToken = "xoxp-5007212458-5029573905-5127214062-7f9749"
botToken = "xoxb-5134150563-itkh6B9inXzlkrCWaBdkCeLS"
itrID = "U053KLMS7"
channelRandom = "C050768H2"
output = []
Matrix = [[0 for x in range(5)] for x in range(5)]
bitteWendenId = "U0539QRF3"

sc = SlackClient(botToken)
if sc.rtm_connect():
    #adds the outputs
    Matrix[0][0] = "Hi"
    Matrix[1][0] = "Hello"

    #sc.rtm_send_message(channelRandom, "Hi")
    dat = sc.api_call("api.test")
    dat2 = sc.api_call("auth.test", token = botToken)


    while True:
        #sc.api_call("users.setPresence", token = botToken, presence = "away")

        for data in sc.rtm_read():
            #print data["type"]
            print sc.server.users
            if "type" in data:
               if data["type"] == "message":
                  chanel = data["channel"]
                  text = data["text"]
                  if text == Matrix[0][0]:
                     sc.api_call("chat.postMessage", channel = chanel, text = "Hello <@{}|{}> <@{}|bittewenden>".format(sc.server.users.find(data["user"]).id, sc.server.users.find(data["user"]).name, bitteWendenId), as_user = True, parse = True)
                #if data["type"] == "user_typing":
                #   output.append("@{} is typing a message".format(sc.server.users.find(data["user"]).name))
                #   sc.rtm_send_message(data["channel"], output[0])
        
        time.sleep(1)
else:
    print "Connection Failed, invalid token?"