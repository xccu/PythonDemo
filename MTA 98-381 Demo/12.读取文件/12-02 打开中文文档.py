#中文会报异常：UnicodeDecodeError
#应当加上encoding='utf8'
f=open('data\poem.txt','r',encoding='utf8')

#打印全文
#content = f.read()

#只打印前7个字符
content = f.read(7)
print(content)