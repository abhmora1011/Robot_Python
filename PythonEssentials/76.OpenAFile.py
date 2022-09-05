from tkinter import *
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(initialdir="C:\\Users\\WONDERS\\Desktop\\training",
                                           title="Open file okay?",
                                           filetypes=(("text files", "*.txt"),
                                           ("all files", "*.*")))
    file = open(file_path, 'r')
    print(file.read())
    file.close()

window = Tk()

button = Button(text="Open", command=open_file)
button.pack()

window.mainloop()
