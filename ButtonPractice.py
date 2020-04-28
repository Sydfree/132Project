import tkinter as tk
import tkinter.messagebox

top = tk.Tk()

def helloCallBack():
    tkinter.messagebox.showinfo("Hello Python", "Hello World")

B = tkinter.Button(top, text = "Hello", command = helloCallBack)

B.pack()
top.mainloop()
