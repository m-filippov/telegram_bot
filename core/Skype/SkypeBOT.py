# -*- coding: utf-8 -*-
from skpy import Skype
from skpy import SkypeAuthException
from datetime import timedelta, datetime
from core import settings
import Comands

time = datetime.now()
timeNow = str(time.strftime("%Y-%m-%d-%H.%M.%S"))

def SendMassedge(massege,chats):

    chats.sendMsg(massege)


def ConectToSkype():

    skype = Skype(connect=False)
    skype.conn.setTokenFile(".token")
    try:
        skype.conn.readToken()
    except SkypeAuthException:
        skype.conn.setUserPwd(settings.SkypeUser, settings.SkypePassword)
        skype.conn.getSkypeToken()
    return skype

def GetMessages(skype):
    msgsGet = skype.getMsgs()
    if len(msgsGet):
        Comands.ComandForSkype(msgsGet[0].content, msgsGet[0].userId, ConectToSkype().chats[settings.TestChat])

def StartBotSkype():
    try:
        print timeNow + " - I`m sart"
        while True:
            GetMessages(ConectToSkype().chats[settings.TestChat])
    except:
        print timeNow + "I`m restart"
        StartBotSkype()
StartBotSkype()
