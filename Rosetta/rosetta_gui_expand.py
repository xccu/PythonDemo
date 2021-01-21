from tkinter import *

#GUI扩展

#label控件，宽高单位：像素
class Label_PX():
    def __init__(self,root,text="",width=60,height=20,bg=None,fg=None, font=None):
        self.frame = Frame(root,width=width,height=height,bg=bg)
        self.frame.pack_propagate(0)
        self.label = Label(self.frame,text=text,bg=bg,fg=fg, font=font)
        self.label.pack()

    def place(self,x,y):
         self.frame.place(x=x,y=y)

#text控件，宽高单位：像素
class Text_PX():
    def __init__(self,root,width=60,height=20,bg=None,fg=None, font=None):
        self.frame = Frame(root,width=width,height=height,bg=bg)
        self.frame.pack_propagate(0)
        self.text = Text(self.frame,width=width,height=height,bg=bg,fg=fg, font=font)
        self.text.pack()

    def place(self,x,y):
         self.frame.place(x=x,y=y)
    
    def insert(self, index, chars, *args):
        self.text.insert(index, chars, *args)
    
    def delete(self, index1, index2=None):
        self.text.delete(index1, index2)

#button控件，宽高单位：像素
class Button_PX():
    def __init__(self,root,text="",width=80,height=30,bg=None,fg=None, font=None,command=None):
        self.frame = Frame(root,width=width,height=height,bg='white')
        self.frame.pack_propagate(0)
        self.button = Button(self.frame,text=text,width=width,height=height,bg=bg,fg=fg,font=font,command=command)
        self.button.pack()

    def place(self,x,y):
         self.frame.place(x=x,y=y)
