import os

filelist=[]
#for root,dirs,files in os.walk('dir'):
#    for name in files:
#        path = os.path.join(root,name)
#        filelist.append(path)
#        print(path)
#dir\非人哉 第81集_1080P在线观看平台_腾讯视频 (1)

for i in range(1,29):
    filelist.append('C:\\Users\\ASUS\\Desktop\\MergeTool\\dir\\{0}.ts'.format(str(i)))
    #print(name)
#for file in filelist:
#    tmp.append(file.replace("\n",""))
    # 合并ts文件
os.chdir("ts/")
shell_str = '+'.join(filelist)
print("cmd")
shell_str = 'copy /b '+ shell_str + ' 5.mp4' #该命令不支持中文
os.system(shell_str)
print(shell_str)
