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
        self.enable=True

    #初始化
    def init(self):
        #设置窗体title
        self.window.title('Rosetta')
        #设置窗体宽高
        self.window.geometry("800x450")
        #self.window.grid(width=80, height=50)

        #self.window.toolbar = Frame(self.window, borderwidth=0)
        self.container = Frame(self.window, relief="sunken", width=800, height=450)
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

        #创建文本框
        self.file_Text = Text(self.container, width=87, height=2)
        #self.file_Text.grid(row=2, column=1,columnspan = 3)
        self.file_Text.place(x=100,y=100)

        #创建日志文本框
        self.log_Text = Text(self.container, width=100, height=10)
        #self.log_Text.grid(row=3, column=0,columnspan = 4)
        self.log_Text.place(x=10,y=150)

        #创建进度条
        self.p_bar = ttk.Progressbar(self.container, length = 705, value = 0, mode = "determinate")
        self.p_bar.place(x=10,y=300)

        #设置进度条回调函数
        self.rsa.callback=self.progress_callback
    
    #加密
    def encrypt_click(self):
        if self.enable:
            _thread.start_new_thread(self.encrypt_thread,())
        else:
            self.log_Text.insert(1.0,'加密程序正在运行中\n')

    #解密
    def decrypt_click(self):
        if self.enable:
            _thread.start_new_thread(self.decrypt_thread,())
        else:
            self.log_Text.insert(1.0,'解密程序正在运行中\n')
            
    #加密函数
    def encrypt_thread(self):
        self.enable=False
        result = self.rsa.encrypt(self.filePath)
        if result=="s_":
            self.log_Text.insert(1.0,'已加密：'+self.filePath+'\n')
        else:
            self.log_Text.insert(1.0,result+'\n')
        self.p_bar["value"]=0
        self.rsa.progress=0
        self.enable=True

    #解密函数
    def decrypt_thread(self):
        self.enable=False
        result = self.rsa.decrypt(self.filePath)
        if result=="s_":
            self.log_Text.insert(1.0,'已解密：'+self.filePath+'\n')
        else:
            self.log_Text.insert(1.0,result+'\n')
        self.p_bar["value"]=0
        self.rsa.progress=0
        self.enable=True

    #进度条回调函数
    def progress_callback(self,i):
        print(i)
        self.p_bar["value"]=i

    #打开文件函数
    def open_file_click(self):
        #self.window.withdraw()

        # 清空文本控件
        self.file_Text.delete('1.0','end')
        # 选择文件
        self.filePath = filedialog.askopenfilename()
        # 显示文件路径
        self.file_Text.insert(1.0,self.filePath)
        #fileUtil=Flie_Util()
        #data = fileUtil.read(self.filePath)
        #self.init_Text.insert(1.0,data)

    #生成密钥函数
    def create_keys_click(self):
        self.rsa.create_rsa_key()
        self.log_Text.insert(1.0,'已生成密钥'+'\n')
