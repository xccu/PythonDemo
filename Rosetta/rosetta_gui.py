from tkinter import *
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

        #创建标签Label
        self.init_Label=Label(self.window,text="加密解密工具",bg='white',relief=GROOVE)
        self.init_Label.grid(row=0, column=0)

        #创建文本框
        self.init_Text = Text(self.window, width=40, height=20)
        self.init_Text.grid(row=1, column=0)

        #创建加密文本框
        self.encrypt_Text = Text(self.window, width=40, height=20)
        self.encrypt_Text.grid(row=1, column=1)

        #加密按钮
        self.encrypt_button = Button(self.window, text="加密", width=10,command=self.encrypt_click)  # 调用内部方法  加()为直接调用
        self.encrypt_button.grid(row=2, column=0)

        #解密按钮
        self.decrypt_button = Button(self.window, text="解密", width=10,command=self.decrypt_click)  # 调用内部方法  加()为直接调用
        self.decrypt_button.grid(row=2, column=1)

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