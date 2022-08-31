from tkinter import *

# label = an area widget that holds text and/or an image within a window

window = Tk()

photo = PhotoImage(file='C:\\Users\\WONDERS\\Desktop\\logo.png')

label = Label(window,
              text="bro, do you even code?",
              font=('Times New Roman', 40, 'italic'),
              fg='#00FF00', # Color
              bg='black',   # Set background color
              relief=RAISED,    # Set border
              bd=10,    # Set the border width
              padx=20,
              pady=20,
              image=photo,  # Add the photo
              compound='bottom'     # combine the text and photo
              )

label.pack()    # To add the label to the window
#   label.place(x=100, y=100)   # To place the label to a certain position

window.mainloop()
