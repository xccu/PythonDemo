import random

s=[]

#计算期望值
for i in range(10): #从0到10遍历
    n=random.randint(1,6)
    s.append(n)
print(s)
result = sum(s)/len(s)
print(result)