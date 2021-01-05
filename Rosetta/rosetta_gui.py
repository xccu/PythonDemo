from tkinter import *
from tkinter import filedialog
from rosetta_core import *

class Init_Window():
    
    #构造函数
    def __init__(self,window):
        self.window = window

    def init(self):
        #设置窗体title
        self.window.title('Python_RUN')
        #设置窗体宽高
        self.window.geometry("800x450")
        #self.window.grid(width=80, height=50)

        #创建标签Label:默认的width, heigth表示字符个数和行数
        self.init_Label=Label(self.window,text="加密解密工具",bg='white',relief=GROOVE,height=1,width=10)
        #self.init_Label.grid(row=0, column=0)
        self.init_Label.place(x=10,y=10)

        #创建文本框
        self.init_Text = Text(self.window, width=50, height=10)
        self.init_Text.place(x=10,y=50)

        #创建加密文本框
        self.encrypt_Text = Text(self.window, width=50, height=10)
        self.encrypt_Text.place(x=400,y=50)

        #加密按钮
        self.encrypt_button = Button(self.window, text="加密", width=10,command=self.encrypt_click)  # 调用内部方法  加()为直接调用
        self.encrypt_button.place(x=10,y=200)

        #解密按钮
        self.decrypt_button = Button(self.window, text="解密", width=10,command=self.decrypt_click)  # 调用内部方法  加()为直接调用
        self.decrypt_button.place(x=100,y=200)

        #保存按钮
        self.decrypt_button = Button(self.window, text="保存", width=10,command=self.save_file_click)  # 调用内部方法  加()为直接调用
        self.decrypt_button.place(x=190,y=200)

        #选择文件按钮
        self.open_file_button = Button(self.window, text="选择文件", width=10,command=self.open_file_click)  # 调用内部方法  加()为直接调用
        self.open_file_button.place(x=10,y=250)

        #创建文本框
        self.file_Text = Text(self.window, width=80, height=2)
        self.file_Text.place(x=100,y=250)

    #加密函数
    def encrypt_click(self):
        #清空文本控件
        self.encrypt_Text.delete('1.0','end')
        #获取文本控件内容
        data = self.init_Text.get("0.0", "end")
        aes = AES_Util()
        self.databyte=aes.encrypt(data)
        encrypt_data = "{}".format(self.databyte)
        self.encrypt_Text.insert(1.0,encrypt_data)

    #解密函数
    def decrypt_click(self):
        #清空文本控件
        self.encrypt_Text.delete('1.0','end')
        aes = AES_Util()
        dataStr=aes.decrypt(self.databyte)
        encrypt_data = "{}".format(dataStr)
        self.encrypt_Text.insert(1.0,encrypt_data)

    #打开文件函数
    def open_file_click(self):
        #self.window.withdraw()
        # 选择文件
        self.filePath = filedialog.askopenfilename()
        # 显示文件路径
        self.file_Text.insert(1.0,self.filePath)
        fileUtil=Flie_Util()
        data = fileUtil.read(self.filePath)
        self.init_Text.insert(1.0,data)

    #保存文件函数
    def save_file_click(self):
        #self.window.withdraw()

        self.filePath=self.filePath.replace('.txt','.rosetta')
        fileUtil=Flie_Util()
        fileUtil.write(self.filePath,self.databyte)
