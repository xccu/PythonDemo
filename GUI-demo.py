from tkinter import *

class Init_Window():
    
    #构造函数
    def __init__(self,window):
        self.window = window

    def init(self):
        #设置窗体title
        self.window.title('Python_RUN')
        #设置窗体宽高
        self.window.geometry("800x450")

        #创建文本框
        self.init_Text = Text(self.window, width=30, height=20)
        self.init_Text.pack(side=TOP,expand=YES, padx=0, pady=0)

        #创建标签Label
        #self.init_Label=Label(root,text="Hello world",bg='white',relief=GROOVE)
        self.init_Label=Label(self.window,text="Hello world",bg='white',relief=GROOVE)
        self.init_Label.pack(side=TOP,expand=YES, padx=0, pady=0)

        #按钮
        self.init_button = Button(self.window, text="你好", bg="lightblue", width=10,command=self.button_click)  # 调用内部方法  加()为直接调用
        self.init_button.pack(side=TOP,expand=YES, padx=0, pady=0)
        #self.init_button.grid(row=1, column=11)

    #功能函数
    def button_click(self):
        print('Hello world')

def main():
    window = Tk()              #实例化出一个父窗口
    ZMJ_PORTAL = Init_Window(window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.init()

    window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示

main()