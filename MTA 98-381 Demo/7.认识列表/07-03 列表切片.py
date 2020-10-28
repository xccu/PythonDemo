score=[68,90,78,95,88,76,100,99,58,60]

#取出下标3~6个元素 打印 [95, 88, 76, 100]
print(score[3:7])
#获取前五个元素 打印 [68, 90, 78, 95, 88]
print(score[0:5])
#获取前五个元素 打印 [68, 90, 78, 95, 88]
print(score[:5])

#赋值列表内存地址
score2=score
#打印 [68,90,78,95,88,76,100,99,58,60]
print(score2)
#is判断两个对象是否是同一对象，打印 True
print(score is score2)

score[0]=100
#打印 100
print(score2[0])
#复制列表内容
score2=score[:]
# 打印False
print(score is score2)
#下标2~6 步长2 打印 [78, 88, 100]
print(score[2:7:2])
#反向下标2~6输出 打印 [99, 100, 76, 88, 95]
print(score[7:2:-1])
#完整的反向输出 打印 [100, 90, 78, 95, 88, 76, 100, 99, 58]
print(score[:-1])