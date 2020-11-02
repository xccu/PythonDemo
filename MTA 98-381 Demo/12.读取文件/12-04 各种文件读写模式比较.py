#r模式，只读 文件不存在则报异常
f=open('data\song.txt','r')
content = f.read()
print(content)
f.close()

#r+模式，读写 文件不存在则报异常
f=open('data\song.txt','r+')
content = f.read()
print(content)
f.write('En Taro Tallnut!')
f.close()

#w模式，只写 文件不存在则创建新文件，文件存在则覆盖原来的内容
f=open('data\song2.txt','w')
f.write('hello')
#报异常 not readable
#content = f.read()
f.close()

#w+模式，读写 文件不存在则创建新文件，文件存在则覆盖原来的内容
f=open('data\song2.txt','w+')
f.write('hello world')
#seek函数 跳到只读位置 0位文件开头
f.seek(0)
content = f.read()
#打印 hello world
print(content)
f.close()

#a模式，只写 文件不存在则创建新文件，在文件末尾追加内容
f=open('data\song3.txt','a')
f.write('hello ')
f.write('world')
#报异常 not readable
#content = f.read()
f.close()

#a+模式，读写 文件不存在则创建新文件，在文件末尾追加内容
f=open('data\song4.txt','a+')
f.write('hello ')
f.write('world')
#seek函数 跳到只读位置 0位文件开头
f.seek(0)
content = f.read()
#打印 hello world
print(content)
f.close()