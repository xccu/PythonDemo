word=input('请输入一个不超过5个字母的单词')
num=1
for letter in word:
    #len判断str长度
    if len(word)>5: 
        print('单词中的字母超过了5个')
        #跳出循环
        break 
    if letter =='-':
        #跳过本次循环并继续
        continue 
    print('Letter {} is {}'.format(num,letter))
    #在循环语句中累加 等价于 num+=1 循环中不能使用++运输符
    num=num+1 
