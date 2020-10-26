#循环输出单个字符
num=1
for letter in 'python':
    print('Letter {} is {}'.format(num,letter))
    num=num+1 #在循环语句中累加 等价于 num+=1 循环中不能使用++运输符

#构造数列 0~9 并打印0 1 2 3 4 5 6 7 8 9
x=range(10)
for i in x:
    print(i,end=' ') #打印末尾设为空格（默认换行）

#打印10次python
for i in range(10):
    print('python',end=' ')