from PIL import Image, ImageTk
import tkinter as tk

IMAGE_PATH = 'netflix.gif'
WIDTH, HEIGTH = 800, 500

root = tk.Tk()
root.geometry('{}x{}'.format(WIDTH, HEIGTH))

canvas = tk.Canvas(root, width=WIDTH, height=HEIGTH)
canvas.pack()

Start = Image.open('Images/maxresdefault.gif')
tk_image = ImageTk.PhotoImage(Start)

img = ImageTk.PhotoImage(Image.open('Images/maxresdefault.gif').resize((WIDTH, HEIGTH), Image.ANTIALIAS))
canvas.background = img  # Keep a reference in case this code is put in a function.
bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)

# Put a tkinter widget on the canvas.
button = tk.Button(root, text="Start")
button_window = canvas.create_window(10, 10, anchor=tk.NW, window=button)

label = tk.Label(canvas,text="Click Here To Start Your Quarantine Adventure!", image=tk_image,compound='center')
label.pack(pady=10,padx=10)
root.mainloop()
