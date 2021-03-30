from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tool_gui_expand import *
import os

class Init_Window():
    
    #构造函数
    def __init__(self,window):
        self.window = window   

        self.pathList = []
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
        self.window.title('Rosetta')
        #设置窗体宽高
        self.window.geometry("800x450")
        #self.window.grid(width=80, height=50)

        #固定宽高，防止用户调整尺寸
        self.window.resizable(0,0) 

        #self.window.toolbar = Frame(self.window, borderwidth=0)
        self.container = Frame(self.window, width=800, height=430)
        self.container.pack()
        #self.container.grid_propagate(False)

        #创建标签Label:默认的width, heigth表示字符个数和行数
        #self.init_Label=Label(self.container,text="加密解密工具",bg='white',height=1,width=10)
        ##self.init_Label.grid(row=0, column=0)
        #self.init_Label.place(x=10,y=10)
        self.init_Label = Label_PX(self.container,text="加密解密工具",width=200,height=20,bg="white")
        self.init_Label.place(x=10,y=10)

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

        #合并按钮
        self.merge_button = Button_PX(self.container, text="合并", width=80,command=self.merge_click)  
        self.merge_button.place(x=280,y=50)

        #清空日志按钮
        #self.import_key_button = Button_PX(self.container, text="清空日志", width=80,command=self.clear_log_click)  
        #self.import_key_button.place(x=370,y=50)

        #选择文件按钮
        self.open_file_button = Button_PX(self.container, text="选择文件", width=80,command=self.open_file_click) 
        self.open_file_button.place(x=10,y=100)

        #选择文件夹按钮
        self.open_folder_button = Button_PX(self.container, text="选择文件夹", width=80,command=self.open_folder_click) 
        self.open_folder_button.place(x=100,y=100)

        #创建路径文本框
        self.file_Text = Text_PX(self.container, width=600, height=25)
        self.file_Text.place(x=190,y=100)



        #创建日志文本框
        #self.log_Text = Text(self.container, width=111, height=15)
        #self.log_Text = Text_PX(self.container, width=780, height=200)
        #self.log_Text.place(x=10,y=150)

        self.file_Listbox  = Listbox(self.container,height=10,width=150)          #  创建两个列表组件
        self.file_Listbox.place(x=10,y=150)

        #for item in self.li:                 # 第一个小部件插入数据
        #    self.file_Listbox.insert(0,item)

        #创建进度条
        #self.p_bar = ttk.Progressbar(self.container, length = 780, value = 0, mode = "determinate")
        #self.p_bar.place(x=10,y=360)

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
        #self.window.withdraw()
        # 清空文本控件
        self.file_Text.delete('1.0','end')
        # 选择文件
        #self.filePath = filedialog.askopenfilename()
        
        self.pathList =filedialog.askopenfilenames()
        for file in self.pathList:   
            self.file_Listbox.insert(END,file)

        self.pathlist = self.file_Listbox.get(0,END)
       
        #self.merge(self.e2)
        # 显示文件路径
        #self.file_Text.insert(1.0,self.filePath)

    #打开文件夹函数
    def open_folder_click(self):
        # 清空文本控件
        self.file_Text.delete('1.0','end')
        # 选择文件夹
        self.filePath = filedialog.askdirectory()
        # 显示文件夹路径
        self.file_Text.insert(1.0,self.filePath)

    def merge_click(self):
        print(self.pathlist)
        os.chdir("ts/")
        self.shell_str = '+'.join(self.pathlist)
        self.shell_str = self.shell_str.replace('/','\\')
        print("cmd")
        self.shell_str = 'copy /b '+ self.shell_str + ' 5.mp4' #该命令不支持中文
        os.system(self.shell_str)
        print(self.shell_str)
