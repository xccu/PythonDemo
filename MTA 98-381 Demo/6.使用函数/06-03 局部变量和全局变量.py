#全局变量
num=50

def func():
    #局部变量，作用域在函数体内
    
    #global将变量num转变为全局变量
    #global num
    num=100
    print(num)

#打印100
func()
#打印50，使用global num后打印100
print(num)