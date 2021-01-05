import tkinter as tk
 
master = tk.Tk()
 
photo = tk.PhotoImage(file ='botton.png')
b = tk.Button(master, text="点我", font = 20, image = photo, compound = "center")
 
b.pack()
 
master.mainloop()