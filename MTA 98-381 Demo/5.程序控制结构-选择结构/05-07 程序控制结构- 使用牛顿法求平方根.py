a=float(input('请输入一个开平方的数字：'))
x=float(input('请输入一个初始数字：'))

while True:
    y=(x+a/x)/2
    if x==y:
        print(y)
        break
    x=y