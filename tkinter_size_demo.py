import tkinter as tk

root = tk.Tk()
root.geometry("800x450")

container = tk.Frame(root, relief="sunken", width=800, height=300,bg="gray")
container.pack()

text_frame = tk.Frame(container,width=200,height=60,bg="white")
text_frame.pack_propagate(0) # Stops child widgets of label_frame from resizing it
tk.Text(text_frame,bg="white",fg="black", font=("Calibri",10)).pack()
text_frame.place(x=10,y=10)

label_frame = tk.Frame(container,width=300,height=20,bg="white")
label_frame.pack_propagate(0) # Stops child widgets of label_frame from resizing it
tk.Label(label_frame,bg="white",fg="black", text = "test",font=("Calibri",12)).pack()
label_frame.place(x=10,y=90)

root.mainloop()