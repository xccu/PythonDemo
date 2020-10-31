#divmod函数 返回商和余数构成的元组
t=divmod(17,5)
#打印 (3, 2)
print(t)

a,b=divmod(17,5)
#打印 3 2
print(a,b)

#计算一元二次方程ax^2+bx+c=0,返回方程的两个解
def quad(a,b,c):
    d=b**2-4*a*c
    if d<0 or a==0:
        return '请重新输入参数！'
    return (-b+d**0.5)/(2*a),(-b-d**0.5)/(2*a)

x=quad(1,-4,4)
print(x)

x1,x2=quad(2,8,5)
print(x1,x2)