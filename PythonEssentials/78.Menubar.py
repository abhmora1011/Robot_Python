from tkinter import *

def open_file():
    print("File has been opened")

def save_file():
    print("File has been saved")

def cut_file():
    print("You cut some text")

def copy_file():
    print("You copy some text")

def paste_file():
    print("You pasted some text")

window = Tk()

openImage = PhotoImage(file="file.png")
saveImage = PhotoImage(file="save.png")
exitImage = PhotoImage(file="exit.png")

menubar = Menu(window)
window.config(menu=menubar)

file_menu = Menu(menubar, tearoff=0, font=("MV Boli", 15) )    # tearoff=0 will remove the line ------- before the options
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file, image=openImage, compound='left')
file_menu.add_command(label="Save", command=save_file, image=saveImage, compound='left')
file_menu.add_separator()   # Add a separator line
file_menu.add_command(label="Exit", command=quit, image=exitImage, compound='left')   # quit is a built-in command

edit_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut_file)
edit_menu.add_command(label="Copy", command=copy_file)
edit_menu.add_command(label="Paste", command=paste_file)

window.mainloop()
