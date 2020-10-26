n=int(input('请输入一个大于1的正整数'))

#当n等于1时，跳出循环
while n!=1:
    print(n)
    if n%2==0:
        n=n/2
    else:
        n=n*3+1