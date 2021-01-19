from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from rosetta_core import *
import _thread
import time

class Init_Window():
    
    #构造函数
    def __init__(self,window):
        self.window = window       
        self.rsa = RSA_Util()
        self.file_util= Flie_Util()
        self.enable=True

    #初始化
    def init(self):
        #设置窗体title
        self.window.title('Rosetta')
        #设置窗体宽高
        self.window.geometry("800x450")
        #self.window.grid(width=80, height=50)

        #固定宽高，防止用户调整尺寸
        self.window.resizable(0,0) 

        #self.window.toolbar = Frame(self.window, borderwidth=0)
        self.container = Frame(self.window, relief="sunken", width=800, height=430)
        self.container.pack()
        self.container.grid_propagate(False)

        #创建标签Label:默认的width, heigth表示字符个数和行数
        self.init_Label=Label(self.container,text="加密解密工具",bg='white',height=1,width=10)
        #self.init_Label.grid(row=0, column=0)
        self.init_Label.place(x=10,y=10)

         #加密按钮
        self.encrypt_button = Button(self.container, text="加密", width=10,command=self.encrypt_click)  # 调用内部方法  加()为直接调用
        #self.encrypt_button.grid(row=1, column=0)
        self.encrypt_button.place(x=10,y=50)

        #解密按钮
        self.decrypt_button = Button(self.container, text="解密", width=10,command=self.decrypt_click) 
        #self.decrypt_button.grid(row=1, column=1)
        self.decrypt_button.place(x=100,y=50)

        #生成密钥按钮
        self.create_key_button = Button(self.container, text="生成密钥", width=10,command=self.create_keys_click) 
        #self.create_key_button.grid(row=1, column=2)
        self.create_key_button.place(x=190,y=50)

        #导入私钥按钮
        self.import_key_button = Button(self.container, text="导入私钥", width=10)  
        #self.import_key_button.grid(row=1, column=3)
        self.import_key_button.place(x=280,y=50)

        #选择文件按钮
        self.open_file_button = Button(self.container, text="选择文件", width=10,command=self.open_file_click) 
        #self.open_file_button.grid(row=2, column=0)
        self.open_file_button.place(x=10,y=100)

        #选择文件夹按钮
        self.open_folder_button = Button(self.container, text="选择文件夹", width=10,command=self.open_folder_click) 
        #self.open_file_button.grid(row=2, column=0)
        self.open_folder_button.place(x=100,y=100)

        #创建路径文本框
        self.file_Text = Text(self.container, width=85, height=2)
        #self.file_Text.grid(row=2, column=1,columnspan = 3)
        self.file_Text.place(x=190,y=100)

        #创建日志文本框
        self.log_Text = Text(self.container, width=111, height=15)
        #self.log_Text.grid(row=3, column=0,columnspan = 4)
        self.log_Text.place(x=10,y=150)

        #创建进度条
        self.p_bar = ttk.Progressbar(self.container, length = 780, value = 0, mode = "determinate")
        self.p_bar.place(x=10,y=360)

        #底部状态栏:信息 
        self.status_bar = Label(self.window, text="就绪", bd=1, relief=SUNKEN,anchor=W,width=100)
        self.status_bar.pack(side=LEFT)

        #底部状态栏:计数 
        self.status_count_bar = Label(self.window, text="", bd=1, relief=SUNKEN,anchor=W)
        self.status_count_bar.pack(side=BOTTOM, fill=X)

        #设置进度条回调函数
        self.rsa.callback=self.progress_callback
    
    #加密按钮响应函数
    def encrypt_click(self):
        if self.enable:
            result=self.file_util.judge_path(self.filePath)
            if result==0:
                _thread.start_new_thread(self.encrypt_folder_thread,())
            elif result==1:
                print("加密文件")
                _thread.start_new_thread(self.encrypt_thread,())
            else :
                self.log_Text.insert(1.0,'未能识别文件或文件夹\n')
        else:
            self.log_Text.insert(1.0,'加密程序正在运行中\n')

    #解密按钮响应函数
    def decrypt_click(self):
        if self.enable:
            result=self.file_util.judge_path(self.filePath)
            if result==0:
                _thread.start_new_thread(self.decrypt_folder_thread,())
            elif result==1:
                _thread.start_new_thread(self.decrypt_thread,())
            else :
                self.log_Text.insert(1.0,'未能识别文件或文件夹\n')
        else:
            self.log_Text.insert(1.0,'解密程序正在运行中\n')
            
    #文件加密线程函数
    def encrypt_thread(self):
        self.enable=False
        self.status_bar["text"] = '加密中：{0}'.format(self.filePath)
        self.status_count_bar["text"] = '1/1'
        self.encrypt(self.filePath)
        self.reset_control()
    
    #文件夹加密线程函数
    def encrypt_folder_thread(self):
        self.enable=False
        flie_list=self.file_util.foreach_folder(self.filePath)
        i=0
        count = len(flie_list)
        for file_name in flie_list:
            i+=1
            self.status_bar["text"] = '加密中：{0}'.format(file_name)
            self.status_count_bar["text"] = '{0}/{1}'.format(i,count)
            self.encrypt(file_name)
        self.log_Text.insert(1.0,'已加密：'+self.filePath+'\n')
        self.reset_control()

    #加密
    def encrypt(self,filePath):
        result = self.rsa.encrypt(filePath)
        if result=="s_":
            self.log_Text.insert(1.0,'已加密：'+filePath+'\n')
        else:
            self.log_Text.insert(1.0,result+'\n')

    #文件解密线程函数
    def decrypt_thread(self):
        self.enable=False
        self.status_bar["text"] = '解密中：{0}'.format(self.filePath)
        self.status_count_bar["text"] = '1/1'
        self.decrypt(self.filePath)
        self.reset_control()
    
    #文件夹解密线程函数
    def decrypt_folder_thread(self):
        self.enable=False
        flie_list=self.file_util.foreach_folder(self.filePath)
        i=0
        count = len(flie_list)
        for file_name in flie_list:
            i+=1
            self.status_bar["text"] = '解密中：{0}'.format(file_name)
            self.status_count_bar["text"] = '{0}/{1}'.format(i,count)
            self.decrypt(file_name)
        self.log_Text.insert(1.0,'已解密：'+self.filePath+'\n')
        self.reset_control()

    #解密
    def decrypt(self,filePath):
        result = self.rsa.decrypt(filePath)
        if result=="s_":
            self.log_Text.insert(1.0,'已解密：'+filePath+'\n')
        else:
            self.log_Text.insert(1.0,result+'\n')
    
    #打开文件函数
    def open_file_click(self):
        #self.window.withdraw()
        # 清空文本控件
        self.file_Text.delete('1.0','end')
        # 选择文件
        self.filePath = filedialog.askopenfilename()
        # 显示文件路径
        self.file_Text.insert(1.0,self.filePath)

    #打开文件夹函数
    def open_folder_click(self):
        # 清空文本控件
        self.file_Text.delete('1.0','end')
        # 选择文件夹
        self.filePath = filedialog.askdirectory()
        # 显示文件夹路径
        self.file_Text.insert(1.0,self.filePath)

    #生成密钥函数
    def create_keys_click(self):
        self.rsa.create_rsa_key()
        self.log_Text.insert(1.0,'已生成密钥'+'\n')

    #进度条回调函数
    def progress_callback(self,i):
        #print(i)
        self.p_bar["value"]=i

    #控件复位函数
    def reset_control(self):
        self.status_bar["text"] = '就绪'
        self.status_count_bar["text"] = ''
        self.p_bar["value"]=0
        self.rsa.progress=0
        self.enable=True