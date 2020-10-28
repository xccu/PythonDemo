sales = [56, 60, 80, 78, 38, 100, 85]
#删除最后一个元素
del sales[-1]
#删除下标为3的元素
del sales[3]
print(sales)

#返回并删除最后一个元素
x= sales.pop()
print(sales,x)

#返回并删除制定下标元素
y= sales.pop(2)
print(sales,y)

sales = [56, 60, 80, 78, 38, 100, 85]
#前两个元素替换为空列表（删除）
sales[:2]=[]
#[80, 78, 38, 100, 85]
print(sales)

#前两个元替换值为[1]
sales[:2]=[1]
#[1, 38, 100, 85]
print(sales)


sales = [56, 60, 80, 78, 38, 60, 85]
#删除列表中第一个为60的元素
sales.remove(60)
#[56, 80, 78, 38, 60, 85]
print(sales)

sales = [56, 60, 80, 78, 38, 60, 85]

#使用循环删除所有60
while True:
    if 60 in sales:
        sales.remove(60)
    else:
        break
#[56, 80, 78, 38, 85]
print(sales)