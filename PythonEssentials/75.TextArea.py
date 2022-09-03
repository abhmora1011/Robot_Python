# text widget = functions like a text area, you can enter multiple lines of text

from tkinter import *

def submit():
    input = text_area.get("1.0", END)
    print(input)

window = Tk()

text_area = Text(window, bg="light yellow", font=("Ink Free", 25), height=8, width=20, pady=20, padx=20, fg="purple")
text_area.pack()

button = Button(window, text="submit", command=submit)
button.pack()

window.mainloop()
