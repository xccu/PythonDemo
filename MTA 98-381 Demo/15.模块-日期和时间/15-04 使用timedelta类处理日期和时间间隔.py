import datetime

t1 = datetime.timedelta(days=3,hours=5)
t2 = datetime.timedelta(hours=3.2)
#时间段相加 打印 3 days, 8:12:00
print(t1+t2)

td = datetime.datetime.today();
t3 = datetime.timedelta(days=100)
#打印今天后的第100天日期
print(td+t3)