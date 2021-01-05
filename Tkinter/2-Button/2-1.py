import tkinter as tk
 
master = tk.Tk()
def callback():
    print("我被调用了！")
 
b = tk.Button(master, text="执行", command=callback)
b.pack()
 
master.mainloop()