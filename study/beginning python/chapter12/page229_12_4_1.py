#!/usr/bin/env python3
__Author__ = "limugen"
import tkinter
# top = tkinter.Tk()
def hello():
    print("hello world")

win = tkinter.Tk()
win.title('hellworld')
win.geometry('200x100')

btn = tkinter.Button(win,text='hello',command=hello)
#btn.pack(expand=YES,fill=BOTH)

win.mainloop()