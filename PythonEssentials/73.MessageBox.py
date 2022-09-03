from tkinter import *
from tkinter import messagebox

def click():

    #   messagebox.showinfo(title="This is an info message box", message="You are a person")
    #   messagebox.showwarning(title="WARNING!", message="You hava a VIRUS!")
    #   messagebox.showerror(title="ERROR!", message="something went wrong")

    # if messagebox.askokcancel(title="ask ok cancel", message="Do you want to do the thing?"):
    #     print("You did a thing!")
    # else:
    #     print("You cancelled a thing!")

    # if messagebox.askretrycancel(title="ask ok cancel", message="Do you want to retry the thing?"):
    #     print("You did a thing!")
    # else:
    #     print("You cancelled a thing!")

    # if messagebox.askyesno(title="Ask yes or no", message="Do you like cake?"):
    #     print("I like cake too")
    # else:
    #     print("Why do you not like cake?")

    # answer = messagebox.askquestion(title="Ask question", message="Do you like pie?")
    # if answer == 'yes':
    #     print("I like pie too!")
    # else:
    #     print("Why? :(")

    # available icons (warning, info, error)
    answer = messagebox.askyesnocancel(title="Yes no cancel", message="Do you like to code?", icon='warning')
    if answer == True:
        print("You like to code!")
    elif answer == False:
        print("Why you are watching a code tutorial?")
    else:
        print("OK!")

window = Tk()

button = Button(window, command=click,text="Click Me")

button.pack()

window.mainloop()