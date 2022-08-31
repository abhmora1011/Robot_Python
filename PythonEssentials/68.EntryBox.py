from tkinter import *

# Entry widget = textbox that accepts a single line of user input

window = Tk()

def submit():
    username = entry.get()
    print("Hello {}".format(username))
    entry.config(state=DISABLED)

def delete():
    entry.delete(0, END)  # Delete all the characters

def backspace():
    entry.delete(len(entry.get())-1, END)  # get the second to last character

entry = Entry(window,
              font=("Arial", 50),
              fg="#00FF00",
              bg="black",
              show="*")

entry.insert(0, "Spongebob") #  Default Value

entry.pack(side=LEFT)

#SUBMIT
submit_button = Button(window,
                       text="Submit",
                       command=submit)

submit_button.pack(side=RIGHT)

# DELETE
delete_button = Button(window,
                       text="Delete",
                       command=delete)

delete_button.pack(side=RIGHT)


# DELETE
backspace_button = Button(window,
                       text="backspace",
                       command=backspace)

backspace_button.pack(side=RIGHT)

window.mainloop()
