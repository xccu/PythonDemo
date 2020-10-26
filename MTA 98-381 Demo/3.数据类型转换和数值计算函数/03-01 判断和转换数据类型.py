x=5
y=3.14
z='007'
#打印 <class 'int'> <class 'float'> <class 'str'>
print(type(x),type(y),type(z))

a=True
b=False
#打印 <class 'bool'> <class 'bool'>
print(type(a),type(b))
#int转float
print(float(x))
#float转int 小数点后舍去（不做四舍五入）
print(int(y),int(3.54))
#str转int 打印 7
print(int(z))
#报错 
#print(int('aaa'))
#其他类型转str 打印 5 3.14 <class 'str'>
print(str(x),str(y),type(str(x)))