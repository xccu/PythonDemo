import tkinter as tk
 
master = tk.Tk()
photo = tk.PhotoImage(file="3.png")
w = tk.Label(master, image=photo)
w.pack()

master.mainloop()