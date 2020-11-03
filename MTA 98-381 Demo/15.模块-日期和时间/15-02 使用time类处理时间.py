import datetime

#时，分，秒，微秒
t=datetime.time(22,11,9,9999)
#打印 22:11:09.009999
print(t)
#打印 00:00:00 23:59:59.999999
print(datetime.time.min,datetime.time.max)