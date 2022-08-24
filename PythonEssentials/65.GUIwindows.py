from tkinter import *

# widgets = GUI elements : buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

window = Tk() #instantiate an instance of a window
window.geometry("600x420")
window.title("Bro Code first GUI program")

icon = PhotoImage(file='C:\\Users\\WONDERS\\Desktop\\logo.png')
window.iconphoto(True, icon)
window.config(background="#AABBEE")

window.mainloop() #place window on computer screen, listen for events