#使用open以读取的方式打开相对路径文件，默认r读取，可省略
#斜杠使用/,//,\均可
f=open('data\song.txt','r')
content = f.read()
#打印 En Taro Tallnut!
print(content)

#使用绝对路径打开文件
f2=open('D:\song.txt','r')
#打印 En Taro Tallnut!
print(f2.read())

#读取文件如果不存在，报异常
#f3=open('data\song3.txt')