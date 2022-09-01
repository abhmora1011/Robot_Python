from tkinter import *

def submit():
    print("The temperature is: " + str(scale.get()) + " degrees celsius")


window = Tk()

#  hot_image = PhotoImage(file='hot.png')
#  hot_label = Label(image=hot_image)
#  hot_label.pack()

scale = Scale(window,
              from_=4000,
              to=0,
              length=400,
              orient=VERTICAL,  # orientation of scale
              font=("Consolas", 20),
              tickinterval=10,  # adds numeric indicators for value
              showvalue=0,  # hide the current value
              resolution=5,
              troughcolor='#69EAFF',
              fg='#FF1C00',
              bg='#111111',
              )
scale.set(((scale['from'] - scale['to'])/2) + scale['to'])
scale.pack()

#  cold_image = PhotoImage(file='hot.png')
#  cold_label = Label(image=hot_image)
#  cold_label.pack()

button = Button(window, text="submit", command=submit)
button.pack()

window.mainloop()
