import random
#产生1到100中间的随机整数
n1 = random.randint(1,100)
print(n1)

#产生1到99中间的随机整数(不包含100)
n2=random.randrange(1,100)
print(n2)

#产生0到100之间5的倍数（步长5）
n3=random.randrange(0,101,5)
print(n3)