# listbox = A listing of selectable text items within it's own container

def submit():
    food = []

    for index in listbox.curselection():
        food.insert(index, listbox.get(index))

    print("You have ordered: ")

    for index in food:
        print(index)


def add():
    listbox.insert(listbox.size(), entrybox.get())
    listbox.config(height=listbox.size())


def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)

    # listbox.delete(listbox.curselection())
    # listbox.config(height=listbox.size())


from tkinter import *

window = Tk()

listbox = Listbox(window,
                  bg="#F7FFDE",
                  font=("Constantia", 35),
                  width=12,
                  selectmode=MULTIPLE)

listbox.pack()

listbox.insert(1, "Pizza")
listbox.insert(2, "Pasta")
listbox.insert(3, "Garlic Bread")
listbox.insert(4, "Soup")
listbox.insert(5, "Salad")

listbox.config(height=listbox.size())

entrybox = Entry(window)
entrybox.pack()

submit_button = Button(window, text="submit", command=submit)
submit_button.pack()

add_button = Button(window, text="add", command=add)
add_button.pack()

delete_button = Button(window, text="delete", command=delete)
delete_button.pack()

window.mainloop()
