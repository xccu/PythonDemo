import os
import os.path 
import shutil

class File_Service():
    def __init__(self):
        self.file_list =[]

    def get_file_expand_name(self,file_name):
        return os.path.splitext(file_name)[1] 

    def copy_file(self,source_file,target_file):
        #print(source_file+' to '+target_file)
        shutil.copyfile(source_file, target_file)

    def create_dir_not_exist(self,path):
        if not os.path.exists(path):
            os.mkdir(path)
    
    def delete_file(self,path):
        for i in os.listdir(path) :# os.listdir(path)#返回一个列表，里面是当前目录下面的所有东西的相对路径
            file_data = path + i#当前文件夹的下面的所有东西的绝对路径
            if os.path.isfile(file_data) == True:#os.path.isfile判断是否为文件,如果是文件,就删除.如果是文件夹.递归给del_file.
                os.remove(file_data)
                print('删除临时文件'+file_data)
            else:
                self.delete_file(file_data)




class Merge_Service():
    def __init__(self,output_path):
        self.output_path = output_path
    
    def merge(self,pathlist):
        print(pathlist)
        os.chdir("ts/")
        #os.chdir(self.output_path)
        self.shell_str = '+'.join(pathlist)
        self.shell_str = self.shell_str.replace('/','\\')
        print("cmd")
        self.shell_str = 'copy /b '+ self.shell_str + ' 5.mp4' #该命令不支持中文
        os.system(self.shell_str)
        print(self.shell_str)