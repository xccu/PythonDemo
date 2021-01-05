import tkinter as tk
 
master = tk.Tk()
longtext = """
Label 可以显示多行文本，你可以直接使用换行符
或使用 wraplength 选项来实现。当文本换行的时
候，你可以使用 anchor 和 justify 选项来使得
文本如你所希望的显示出来。
"""

w = tk.Label(master, text=longtext, anchor="w", justify="left")
w.pack()
 
master.mainloop()