

import tkinter as tk
#import tkfont

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        #self._textFont = tkFont.Font(name="TextFont")
        #self._textFont.configure(**tkFont.nametofont("TkDefaultFont").configure())

        toolbar = tk.Frame(self, borderwidth=0)
        container = tk.Frame(self, borderwidth=1, relief="sunken", width=800, height=450)
        container.grid_propagate(False)
        toolbar.pack(side="top", fill="x")
        container.pack(side="bottom", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        text = tk.Text(container, font="TextFont",width=100,height=20)
        text.grid(row=0, column=0, sticky="nsew")

        zoomin = tk.Button(toolbar, text="+", command=self.zoom_in)
        zoomout = tk.Button(toolbar, text="-", command=self.zoom_out)
        zoomin.pack(side="left")
        zoomout.pack(side="left")

        text.insert("end", '''Press te + and - buttons to increase or decrease the font size''')

    def zoom_in(self):
        print("")
        #font = tkFont.nametofont("TextFont")
        #size = font.actual()["size"]+2
        #font.configure(size=size)

    def zoom_out(self):
        print("")
        #font = tkFont.nametofont("TextFont")
        #size = font.actual()["size"]-2
        #font.configure(size=max(size, 8))



if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()


