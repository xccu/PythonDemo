from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tool_gui_expand import *
from tool_service import *
import os

class Init_Window():
    
    #构造函数
    def __init__(self,window):
        self.window = window   
       

        self.temp_path = 'd:\\target\\temp\\'   #临时文件夹
        self.output_path='d:\\target\\output\\' #导出文件夹
        self.curPath = os.path.abspath(os.path.dirname(__file__)) #项目所在文件夹
        self.folder=''

        self.file_service= File_Service()
        self.merge_service = Merge_Service(self.output_path)
    
        #self.config = Config()
        #encrypt_str="{0}_Encryptor".format( self.config.get_option("Encrypt","type"))
        #print(encrypt_str) 
        #通过类名反射获取encryptor
        #self.encryptor = globals()[encrypt_str]()
        #self.file_util= Flie_Util()
        self.enable=True


    #初始化
    def init(self):
        #设置窗体title
        self.window.title('文件合并工具')
        #设置窗体宽高
        self.window.geometry("800x450")
        #self.window.grid(width=80, height=50)

        #固定宽高，防止用户调整尺寸
        self.window.resizable(0,0) 

        #self.window.toolbar = Frame(self.window, borderwidth=0)
        self.container = Frame(self.window, width=800, height=430)
        self.container.pack()
        #self.container.grid_propagate(False)

        #加密按钮
        #self.encrypt_button = Button(self.container, text="加密", width=10,command=self.encrypt_click)  # 调用内部方法  加()为直接调用
        #self.encrypt_button = Button_PX(self.container, text="加密", width=23,height = 23,image="img/encrypt.png", relief = "solid",bd = 1,command=self.encrypt_click)
        #self.encrypt_button.place(x=10,y=50)

        #解密按钮
        #self.decrypt_button = Button_PX(self.container, text="解密", width=23,height = 23,image="img/decrypt.png", relief = "solid",bd = 1, command=self.decrypt_click) 
        #self.decrypt_button.place(x=35,y=50)

        #生成密钥按钮
        #self.create_key_button = Button_PX(self.container, text="生成密钥",width=23,height = 23,image="img/create-key.png", relief = "solid",bd = 1, command=self.create_keys_click) 
        #self.create_key_button.place(x=60,y=50)

        #导出列表按钮
        self.export_list_button = Button_PX(self.container, text="导出列表", width=80,command=self.export_list_click)  
        self.export_list_button.place(x=10,y=20)

        #导入列表按钮
        self.import_list_button = Button_PX(self.container, text="导入列表", width=80,command=self.import_list_click)  
        self.import_list_button.place(x=100,y=20)

        #清空列表按钮
        self.clear_list_button = Button_PX(self.container, text="清空列表", width=80,command=self.clear_list_click)  
        self.clear_list_button.place(x=190,y=20)

        #选择文件按钮
        self.open_file_button = Button_PX(self.container, text="选择文件", width=80,command=self.open_file_click) 
        self.open_file_button.place(x=280,y=20)

        #合并按钮
        self.merge_button = Button_PX(self.container, text="合并", width=80,command=self.merge_click)  
        self.merge_button.place(x=370,y=20)

        #测试按钮
        #self.open_folder_button = Button_PX(self.container, text="测试", width=80,command=self.open_folder_click) 
        #self.open_folder_button.place(x=280,y=20)

        
        self.temp_path = self.curPath+'\\temp\\'

        #rootPath = curPath[:curPath.find("myProject\\")+len("myProject\\")]  # 获取myProject，也就是项目的根路径
        #dataPath = os.path.abspath(rootPath + 'data\\train.csv') # 获取tran.csv文件的路径

        self.init_Label = Label_PX(self.container,text="导出文件夹",width=60,height=20)
        self.init_Label.place(x=10,y=80)

        #导出文件夹路径文本框
        self.file_Text = Text_PX(self.container, width=700, height=25)
        self.file_Text.place(x=80,y=80)
        self.file_Text.insert(1.0,self.output_path)

        # 创建列表组件
        self.file_Listbox  = Listbox(self.container,height=15,width=110)          
        self.file_Listbox.place(x=10,y=130)

        #底部状态栏:信息 
        self.status_bar = Label(self.window, text="就绪", bd=1, relief=SUNKEN,anchor=W,width=100)
        self.status_bar.pack(side=LEFT)

        #底部状态栏:计数 
        self.status_count_bar = Label(self.window, text="", bd=1, relief=SUNKEN,anchor=W)
        self.status_count_bar.pack(side=BOTTOM, fill=X)

        #设置进度条回调函数
        #self.encryptor.progress_func=self.progress_callback
    
    #打开文件函数
    def open_file_click(self):
        # 选择文件
        file_list =filedialog.askopenfilenames()
        #文件列表写入给file_Listbox控件
        for file in file_list:   
            self.file_Listbox.insert(END,file)

    #测试函数
    def open_folder_click(self):
         #os.remove('d:\\target\\temp\\1.ts')
         print('test')

    def merge_click(self):
        self.path_list = self.file_Listbox.get(0,END)
        files= []
        i=1
        for file in self.path_list:  
            if file=='':
                continue
            if not(self.folder == ''):
                file =  '{0}\\{1}'.format(self.folder,file)
            print(file)
            expand_name = self.file_service.get_file_expand_name(file)
            target_file = '{0}{1}{2}'.format(self.temp_path,i,expand_name)  
            i+=1
            files.append(target_file)
            self.file_service.copy_file(file,target_file)
        self.merge_service.merge(files)
        self.file_service.delete_file(self.temp_path)

    #导出列表按钮响应函数
    def export_list_click(self):
        # 选择文件夹
        export_path = filedialog.askdirectory()
        export_list = self.file_Listbox.get(0,END)
        data=''
        for file in export_list:  
            data += file.split('/')[-1]+'\n'
        self.file_service.write(export_path+'/test.li',data)

    #导入列表按钮响应函数
    def import_list_click(self):
        # 选择文件
        path =filedialog.askopenfilename()
        self.folder= os.path.split(path)[0].replace('/','\\')  
        print(self.folder)     
        files = self.file_service.read(path)
        file_list = files.split('\n')
        self.file_Listbox.delete(0,END)
        for file in file_list:  
            if file=='':
                continue 
            self.file_Listbox.insert(END,file)

    #清空列表按钮响应函数
    def clear_list_click(self):
        self.file_Listbox.delete(0,END)