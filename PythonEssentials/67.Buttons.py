from tkinter import *

# button =  you click it and then does stuff

window = Tk()

count = 0

photo = PhotoImage(file='C:\\Users\\WONDERS\\Desktop\\logo.png')

def click():
    global count
    count += 1
    print(count)

button =  Button(window,
                 text="Click Me!",
                 command=click,
                 font=("Times New Roman", 30),
                 fg="blue",
                 bg="black",
                 activeforeground="#00FF00",
                 activebackground="black",
                 state=ACTIVE,     # To able/disable the button
                 image=photo,
                 compound="top"
                 )

button.pack()

window.mainloop()