n=[1,2,3,4,5,6]
s='python'

#zip函数组成成对的元组,以最短的序列为准
for pair in zip(n,s):
    print(pair)

for x,y in zip(n,s):
    print(x,y)

#enumerate产生自带索引的元组（默认0开始）
for i in enumerate(s):
    print(i)

#enumerate产生自带索引的元组（1开始）
for i,j in enumerate(s,start=1):
    print(i,j)