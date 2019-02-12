# -*- coding: utf-8 -*-
from skpy import Skype
from skpy import SkypeAuthException
from datetime import timedelta, datetime
from core import changelog
from core import settings

def ConectToSkype():

    skype = Skype(connect=False)
    skype.conn.setTokenFile(".token")
    try:
        skype.conn.readToken()
    except SkypeAuthException:
        skype.conn.setUserPwd(settings.SkypeUser, settings.SkypePassword)
        skype.conn.getSkypeToken()
    return skype

def SendMassedge(massege,chats):

    chats.sendMsg(massege)

def GetMessages(skype):
    timeNow = datetime.now() - timedelta(hours=2, minutes=2)
    msgsGet = skype.getMsgs()
    #        print msgsGet[0].content

    if len(msgsGet) and "$build" in msgsGet[0].content and msgsGet[0].time > timeNow:
        SendMassedge("ok", skype)
        changelog.ChangeLog(settings.PatchToChangelog)

def StartBotSkype():
    while True:
        GetMessages(ConectToSkype().chats[settings.TestChat])
    else:
        ConectToSkype()




#        print chats.getMsgs()
StartBotSkype()
#[SkypeNewMessageEvent(id=1057, type=u'NewMessage', time=datetime.datetime(2019, 2, 4, 16, 21, 55), msgId=1549297315934L)]