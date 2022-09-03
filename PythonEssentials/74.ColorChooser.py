from tkinter import *
from tkinter import colorchooser

def click():
    color = colorchooser.askcolor()
    #   print(color)
    #   color_hex = color[1]    # to get the hex value and not the RGB
    #   print(color_hex)
    window.config(bg=color[1])

window = Tk()

window.geometry("420x420")

button = Button(text="Click Me!", command=click)

button.pack()

window.mainloop()
