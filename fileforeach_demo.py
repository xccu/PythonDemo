import os

#遍历指定文件夹中所有文件
def foreachFiles(path):
    for root,dirs,files in os.walk(path):
        for name in files:
            print(os.path.join(root,name))
 
path=r"D:\mybatis-plus-doc"
foreachFiles(path)