import tkinter as tk
 
master = tk.Tk()
v = tk.StringVar()
w = tk.Label(master, textvariable=v)
v.set("~新的文本~")
w.pack()

master.mainloop()