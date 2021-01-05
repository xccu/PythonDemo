import tkinter as tk
 
master = tk.Tk()
 
photo = tk.PhotoImage(file ='botton.png')
b = tk.Button(master, text="点它 ->", font = 20, image = photo, compound = "right")
 
b.pack()
 
master.mainloop()