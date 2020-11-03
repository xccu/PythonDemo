#导入datetime模块
import datetime

#范围：1-9999年 打印 1 9999
print(datetime.MINYEAR,datetime.MAXYEAR)
#打印 2000-09-01
print(datetime.date(2000,9,1))
#打印当前日期 格式yyyy-MM-dd
print(datetime.date.today())
td = datetime.date.today()
#分别打印年，月，日
print(td.year,td.month,td.day)
#打印当前的星期
#weekday()从0开始, isoweekday从1开始
print(td.weekday(),td.isoweekday())