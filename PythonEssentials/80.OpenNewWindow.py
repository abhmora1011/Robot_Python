from tkinter import *

def create_new_window():
    new_window = Tk()       # TopLevel() = new window on top of other windows, linked to a bottom window
                            # Tk() = new independent window
    old_window.destroy()    # close out of old window

old_window = Tk()

Button(old_window, text="Create new window", command=create_new_window).pack()

old_window.mainloop()
