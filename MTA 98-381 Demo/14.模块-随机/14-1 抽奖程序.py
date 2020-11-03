x = ['zwzig','tom','mary','hofmann','merkel','mike']

#导入random模块
import random
#从列表中随机抽取
a=random.choice(x)
print(a)

#使用rd代表random
import random as rd 
#从列表中随机抽取3个元素
b=rd.sample(x,3)
print(b)

#省略random的用法
from random import *
c=sample(x,2)
print(c)