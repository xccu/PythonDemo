x=3
y=5

#使用元组实现变量交换
x,y = y,x
#打印 5 3
print(x,y)

#使用元组给多个变量赋值
a,b,c = (1,3,5)
#打印 1 3 5
print(a,b,c)

username,domain = '123@qq.com'.split('@')
#打印 123 qq.com
print(username,domain)

#通过列表赋值
m,n=['China','Japan']
#打印 China Japan
print(m,n)