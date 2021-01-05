import tkinter as tk
 
master = tk.Tk()
def callback():
    print("我被调用了！")
 
longtext = """
我明明只是一个按钮，
作为按钮并不需要太多
的文字用于告诉用户当
我被按下的时候会发生
什么事情，但我为什么
这么长？
"""
b = tk.Button(master, text=longtext, anchor="w", justify="left", padx=2, command=callback)
b.pack()
b.config(relief="sunken")
 
master.mainloop()