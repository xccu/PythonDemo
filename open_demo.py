import tkinter as tk
from tkinter import filedialog

#打开文件对话框
def open():
    root = tk.Tk()
    root.withdraw()
    # 选择文件夹
    #Folderpath = filedialog.askdirectory()
    # 选择文件
    Filepath = filedialog.askopenfilename()
    # 打印文件夹路径
    #print('Folderpath:', Folderpath)
    # 打印文件路径
    print('Filepath:', Filepath)

if __name__ == '__main__':
    open()