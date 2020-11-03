import datetime

dt = datetime.datetime(2020,9,1,8,30,15,1000)
#打印 2020-09-01 08:30:15.001000
print(dt)
#打印 0001-01-01 00:00:00 9999-12-31 23:59:59.999999
print(datetime.datetime.min,datetime.datetime.max)
#打印当前时间（到微秒）
print(datetime.datetime.now())
#打印当前日期
print(datetime.date.today())