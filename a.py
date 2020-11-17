from tkinter import *
class A(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        container=Frame(self)
        container.pack(side='top',fill='both',expand='True')
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        self.frames={}
        for F in (a,b,c):
            page_name=F.__name__
            frame=F(parent=container,controller=self)
            self.frames[page_name]=frame
            frame.grid(row=0,column=0,sticky='nsew')
        self.show_frame('a')
    def show_frame(self,page_name):
        frame=self.frames[page_name]
        frame.tkraise()
class a:
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        self.controller=controller
class b:
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        self.controller=controller
class c:
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        self.controller=controller
if __name__=='__main__':
    a1=A()
    a1.mainloop()