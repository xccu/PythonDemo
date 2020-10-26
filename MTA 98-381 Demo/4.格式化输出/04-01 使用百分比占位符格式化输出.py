start_num=1
end_num=100

#打印 count from 1 to 100 .
print('count from',start_num,'to',end_num,'.')
#打印 count from 1 to 100.
print('count from '+str(start_num)+' to '+str(end_num)+'.')

#使用占位符格式化打印（整型变量）
print('count from %d to %d.'%(start_num,end_num))
#使用占位符格式化打印（保留两位的浮点型变量）
print('count from %.2f to %.2f.'%(start_num,end_num))