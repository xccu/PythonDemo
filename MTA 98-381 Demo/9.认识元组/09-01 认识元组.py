#元组定义和初始化
countries='China','Japan','Germany','France','America','Canada'
countries2=('China','Japan','Germany','France','America','Canada')
#打印 True
print(countries==countries2)

#只包含一个元素的元组
country=('China',)
#打印 ('China',) 切片使用和列表相同
print(country)
#打印 Japan
print(countries[1])
#打印 ('China', 'Japan', 'Germany')
print(countries[:3])

#创建空的元组
t = tuple()
#打印 ()
print(t)
#打印 ('p', 'y', 'h', 't', 'o', 'n')
print(tuple('pyhton'))

#元组的不可修改
#报错 TypeError: 'tuple' object does not support item assignment
#countries[5]='USA'

#创建新元组并改变旧元组的元素：旧元组截取到倒数第二位并加入新元组
countries_new=countries[:-1]+('USA',)
#打印 ('China', 'Japan', 'Germany', 'France', 'America', 'USA')
print(countries_new)