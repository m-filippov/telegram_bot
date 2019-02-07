# -*- coding: utf-8 -*-
from skpy import Skype
from skpy import SkypeAuthException
from skpy import SkypeEventLoop
from skpy import SkypeTextMsg
import datetime
from core import changelog
from core import settings


sk = Skype(connect=False)
sk.conn.setTokenFile(".token")
try:
    sk.conn.readToken()
except SkypeAuthException:
    sk.conn.setUserPwd("xmelayx@gmail.com", "Zevs00807")
    sk.conn.getSkypeToken()
#        sk = Skype(tokenFile="/home/gitlab-runner/.tokens-fred.2")
ch = sk.chats["19:42bd94aef87c496c88067ae137c4b998@thread.skype"]
#get = sk.chats["19:42bd94aef87c496c88067ae137c4b998@thread.skype"].getMsgs()
#ch.sendMsg("test")
class MySkype(SkypeEventLoop):
    def onEvent(self, event):
        print(repr(event))


def SendMassedge(massege,chats):

    chats.sendMsg(massege)

def GetMassedge(chats):
    skype = MySkype(tokenFile=".token", autoAck=True)

    while True:

#        Event = str(chats.getMsgs())
        date = skype.onEvent(chats.getMsgs())
        print (date)





#        if "$build" in Event:
#                if tail in"".join(map(str, chats.getMsgs())):
#                SendMassedge("ok", ch)
#                changelog.ChangeLog(settings.PatchToChangelog)
#        print Event

#        print chats.getMsgs()
GetMassedge(ch)
#[SkypeNewMessageEvent(id=1057, type=u'NewMessage', time=datetime.datetime(2019, 2, 4, 16, 21, 55), msgId=1549297315934L)]