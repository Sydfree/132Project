##import tkinter as tk
##import tkinter.messagebox
##
##top = tk.Tk()
##
##def helloCallBack():
##    tkinter.messagebox.showinfo("Hello Python", "Hello World")
##    
##
##B = tkinter.Button(top, text = "Hello", command = helloCallBack)
##C = tkinter.Button(top, text = "Test", command = helloCallBack)
##
##B.pack()
##C.pack()
##top.mainloop()

import tkinter as tkinter
import random
class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.button1 = tkinter.Button(self.main_window,text='Average',command=self.average)
        self.button1.pack()
        tkinter.mainloop()
    def average(self):
        self.mini_window = tkinter.Toplevel()
        self.avg_mess = tkinter.Label(self.mini_window,text='Results:')
        self.avg_result_var = tkinter.StringVar()
        self.avg_result_display = tkinter.Label(self.mini_window,textvariable=self.avg_result_var)
        self.avg_mess.pack(fill="both")
        self.avg_result_display.pack()
        self.button2 = tkinter.Button(self.mini_window,text='Calculate',command=self.avg_calc)
        self.button2.pack()
    def avg_calc(self):
        x = random.randint(100,200)
        self.avg_result = (100+300+x)/3
        print("result:", self.avg_result)
        self.avg_result_var.set(self.avg_result)
gui = MyGUI()
