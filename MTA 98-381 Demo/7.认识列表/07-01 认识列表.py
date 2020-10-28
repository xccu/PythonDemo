#列表的写法：中括号
#字符串列表
namelist=['mary','mike','tom']
#整数型列表
scorelist=[67,90,78]
#混合型列表
namelist_score=['mary','mike','tom',67,90,78]
#打印 <class 'list'> <class 'list'> <class 'list'>
print(type(namelist),type(scorelist),type(namelist_score))

#空列表
empty=[]
#打印 <class 'list'>
print(type(empty))

#列表嵌套
countries=[
    ['China','Japan'],
    ['Germany','France'],
    ['America','Canada']
]
