from datetime import timedelta
import datetime
from skpy import SkypeTextMsg
from skpy import SkypeMsg
import re
a = [SkypeTextMsg(id=u'1549370796893', type=u'Text', time=datetime.datetime(2019, 2, 5, 12, 46, 36, 886000), clientId=u'1549370796898', userId=u'live:xmelayx_1', chatId=u'19:42bd94aef87c496c88067ae137c4b998@thread.skype', content=u'ok'), SkypeTextMsg(id=u'1549370792596', type=u'Text', time=datetime.datetime(2019, 2, 5, 12, 46, 32, 589000), clientId=u'1549370792445', userId=u'live:xmelayx_1', chatId=u'19:42bd94aef87c496c88067ae137c4b998@thread.skype', content=u'ok'), SkypeTextMsg(id=u'1549370792065', type=u'Text', time=datetime.datetime(2019, 2, 5, 12, 46, 32, 42000), clientId=u'1549370792046', userId=u'live:xmelayx_1', chatId=u'19:42bd94aef87c496c88067ae137c4b998@thread.skype', content=u'ok'), SkypeTextMsg(id=u'1549370789158', type=u'Text', time=datetime.datetime(2019, 2, 5, 12, 46, 29, 152000), clientId=u'1549370789158', userId=u'live:xmelayx_1', chatId=u'19:42bd94aef87c496c88067ae137c4b998@thread.skype', content=u'ok'), SkypeTextMsg(id=u'1549370788908', type=u'Text', time=datetime.datetime(2019, 2, 5, 12, 46, 28, 902000), clientId=u'1549370788909', userId=u'live:xmelayx_1', chatId=u'19:42bd94aef87c496c88067ae137c4b998@thread.skype', content=u'ok'), SkypeTextMsg(id=u'1549370788705', type=u'Text', time=datetime.datetime(2019, 2, 5, 12, 46, 28, 699000), clientId=u'1549370788708', userId=u'live:xmelayx_1', chatId=u'19:42bd94aef87c496c88067ae137c4b998@thread.skype', content=u'ok'), SkypeTextMsg(id=u'1549370788549', type=u'Text', time=datetime.datetime(2019, 2, 5, 12, 46, 28, 558000), clientId=u'1549370788559', userId=u'live:xmelayx_1', chatId=u'19:42bd94aef87c496c88067ae137c4b998@thread.skype', content=u'ok'), SkypeTextMsg(id=u'1549370788408', type=u'Text', time=datetime.datetime(2019, 2, 5, 12, 46, 28, 402000), clientId=u'1549370788409', userId=u'live:xmelayx_1', chatId=u'19:42bd94aef87c496c88067ae137c4b998@thread.skype', content=u'ok'), SkypeTextMsg(id=u'1549370788221', type=u'Text', time=datetime.datetime(2019, 2, 5, 12, 46, 28, 183000), clientId=u'1549370788188', userId=u'live:xmelayx_1', chatId=u'19:42bd94aef87c496c88067ae137c4b998@thread.skype', content=u'ok'), SkypeTextMsg(id=u'1549370788002', type=u'Text', time=datetime.datetime(2019, 2, 5, 12, 46, 27, 996000), clientId=u'1549370788002', userId=u'live:xmelayx_1', chatId=u'19:42bd94aef87c496c88067ae137c4b998@thread.skype', content=u'ok')]
b = [(SkypeTextMsg(id=u'1549370796893', type=u'Text', time=datetime.datetime(2019, 2, 7, 13, 27, 36, 886000),))]
c = []
#print b
#if len(a):
#  data = re.split("\n", b)[3]
#  reg = re.compile(('[A-Za-z]'))
#  time1 = reg.sub('', data)
#  for s in ['-', ':', '.']:
#      if s in time1:
#          time1 = time1[2:].replace(s, ", ")
#  print time1
#          time1l = re.split(', ', time1)
#  print time1l
#  print int(time1[3:])
#  T2 = [time1(map(int, x)) for x in time1]
#  print time1[2:].replace("-", ", ",)
#else:
#    print "e"

now = datetime.datetime.now() - timedelta(hours=2, minutes=2)

msgTime = b[0].time
if msgTime > now:
    print "ok"
else:
    print "no"

update_date = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#print update_date
now = datetime.datetime.now() - timedelta(hours=2, minutes=2)
#print now
time=datetime.datetime(2019, 2, 7, 15, 26, 00, 893000)
#print time
#if time > now:
#    print "ok"
#else:
#    print "no"