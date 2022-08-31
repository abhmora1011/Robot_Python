from tkinter import *

# Checkboxes

def display():
    if x.get():
        print("You agree")
    else:
        print("You don't agree")

window = Tk()

icon = PhotoImage(file='C:\\Users\\WONDERS\\Desktop\\logo.png')

x = BooleanVar() #  If this will return and integer IntString if String

check_btn = Checkbutton(window,
                        text="I agree to the terms and condition",
                        variable=x,
                        onvalue=True,
                        offvalue=False,
                        command=display,
                        font=("Arial", 20),
                        fg="#00FF00",
                        bg="black",
                        activebackground="black",
                        activeforeground="#00FF00",
                        padx=25,
                        pady=10,
                        image=icon,
                        compound="left")

check_btn.pack()

window.mainloop()

