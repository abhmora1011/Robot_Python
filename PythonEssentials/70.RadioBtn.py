# radio button - similar to checkbox, but you can only select one from a group

from tkinter import *

food = ["pizza", "hamburger", "hotdog"]

def order():
    if x.get() == 0:
        print("You order pizza!")
    elif x.get() == 1:
        print("You order hamburger!")
    else:
        print("You order hotdog!")

window = Tk()

pizza_image = PhotoImage(file="")
hamburger_image = PhotoImage(file="")
hotdog_image = PhotoImage(file="")

food_images = [pizza_image, hamburger_image, hotdog_image]

x = IntVar()

for index in range(len(food)):
    radiobtn = Radiobutton(window,
                           text=food[index],    # add text to radio btns
                           variable=x,  # groups radio buttons together if they share the same variable
                           value=index,  # assign each radio button a different value
                           padx=25,  # adds padding on x-axis
                           font=("Impact", 30),
                           #  image=food_images[index],  # add images to radio button
                           compound='left',  # add image and text (left-side)
                           indicatoron=0,  # eliminate circle indicators
                           width=75,  # sets width of radio buttons
                           command=order  # set command of radio button to a function
                           )
    radiobtn.pack(anchor=W)

window.mainloop()
