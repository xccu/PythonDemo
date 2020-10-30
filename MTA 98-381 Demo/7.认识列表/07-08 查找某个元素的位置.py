sales = [50,55,51,79,92,100,55,80,55,77]

#返回第一个55的索引 打印 1
print(sales.index(55))

n=1
for i in range(len(sales)):
    if sales[i]==55:
        print('第{}个55的位置是{}'.format(n,i+1))
        n+=1 