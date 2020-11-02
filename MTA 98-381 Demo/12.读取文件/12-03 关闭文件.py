#中文会报异常：UnicodeDecodeError
#应当加上encoding='utf8'
f=open('data\poem.txt','r',encoding='utf8')

#只打印前7个字符
content = f.read(7)
#关闭文件，释放内存
f.close()

print(content)

#with代码块自动释放资源，类似于c#的using
with open('data\poem.txt','r',encoding='utf8') as f_obj:
    content = f_obj.read()
    print(content)