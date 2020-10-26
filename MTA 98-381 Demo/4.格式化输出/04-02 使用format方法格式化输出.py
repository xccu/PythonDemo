name='Tom'
start_num=1
end_num=100

#format格式化输出 打印 Tom is a boy. Tom can count from 1 to 100.
print('{} is a boy. {} can count from {} to {}.'.format(name,name,start_num,end_num))
#format下标格式化输出
print('{0} is a boy. {0} can count from {1} to {2}.'.format(name,start_num,end_num))

x=0.1
y=0.2
#{:.2f} 浮点型保留两位小数
print('{:.2f}+{:.2f}={:.2f}'.format(x,y,x+y))