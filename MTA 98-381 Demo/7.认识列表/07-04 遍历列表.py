num=[1,3,5,7,9]
n=1

#遍历输出
for i in num:
    print('第{}个元素的平方是{}'.format(n,i**2))
    n+=1

#遍历修改元素
for i in range(len(num)):
    num[i]=num[i]**2

#打印 [1, 9, 25, 49, 81]
print(num)