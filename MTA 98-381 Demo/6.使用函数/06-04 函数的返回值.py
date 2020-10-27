def print_stern(symbol):
    i=1
    #从1到11遍历，步长为2
    for i in range(1,11,2):
        #格式{:^11} 居中对其，长度11位
        print('{:^11}'.format(symbol*i))

print_stern('$')

#导入库
import math

#带返回值的函数
def area(r):
    #等价于 math.pi*pow(r,2)
    a=math.pi*(r**2)
    return a

print(area(5))

def cylinder_volume(s,h):
    return s*h

print(cylinder_volume(area(5),10))