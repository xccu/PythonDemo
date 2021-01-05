import tkinter as tk
 
master = tk.Tk()
def callback():
    print("我被调用了！")
 
f = tk.Frame(master, height=64, width=64)
f.pack_propagate(0)
f.pack()
 
b = tk.Button(f, text="确定", command=callback)
b.pack(fill="both", expand=1)
 
master.mainloop()