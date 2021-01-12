import tkinter as tk
import time
import threading
from tkinter import ttk


window = tk.Tk()
# 设置窗口大小
winWidth = 600
winHeight = 400
# 获取屏幕分辨率
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
 
x = int((screenWidth - winWidth) / 2)
y = int((screenHeight - winHeight) / 2)
 
# 设置主窗口标题
window.title("ProgressBar参数说明")
# 设置窗口初始位置在屏幕居中
window.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
# 设置窗口图标
#window.iconbitmap("./image/icon.ico")
# 设置窗口宽高固定
window.resizable(0, 0)
 
""" Progressbar参数
 
        STANDARD OPTIONS
            class, cursor, style, takefocus
 
        WIDGET-SPECIFIC OPTIONS
            orient, length, mode, maximum, value, variable, phase
 """
 
pb = ttk.Progressbar(window, length = 400, value =0, mode = "determinate")
pb.pack(pady = 10)
 




def start_thread():
    for i in range(100):
        pb["value"] = i+1
        time.sleep(0.1)
    pb["value"]=0

def start(): 
    #在新线程启动
    t = threading.Thread(target=start_thread)
    t.start()

tk.Button(window, text="开始", command=start).pack()

window.mainloop()