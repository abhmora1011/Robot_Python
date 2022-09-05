from tkinter import *
from tkinter import filedialog

def save_file():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\WONDERS\\Desktop\\training",
                                    defaultextension=".txt",
                                    filetypes=[
                                        ("Text file", ".txt"),
                                        ("HTML file", ".html"),
                                        ("All files", "*.*")
                                    ])
    if file is None:    # to rid off the exception error when not entering a
        return
    # file_text = str(text.get(1.0, END))
    file_text = input("Enter some test I guess")  # To use the console to write the text
    file.write(file_text)
    file.close()

window = Tk()

button = Button(text="Save", command=save_file)
button.pack()

text = Text(window)
text.pack()

window.mainloop()
