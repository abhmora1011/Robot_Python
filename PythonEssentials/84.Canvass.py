# canvass widget that is used to draw graphs, plots, images in a window

from textwrap import fill
from tkinter import *
from turtle import width

window = Tk()

canvass =  Canvas(window, height=500, width=500)

canvass.create_line(0,0,500,500, fill="blue", width=5)

canvass.create_line(0,500,500,0, fill="red", width=5)

canvass.create_rectangle(50,50,250,250,fill="cyan")

points = [250,0,500,500,0,500]

canvass.create_polygon(points, fill="yellow", outline="black", width=5)

# canvass.create_arc(0, 0, 500, 500, fill="green", style=PIESLICE, start=270, extent=180)

canvass.create_arc(0,0,500,500,fill="red", extent=180, width=10)
canvass.create_arc(0,0,500,500,fill="white", extent=180, width=10, start=180)
canvass.create_oval(190,190,310,310, fill="white", width=10)

canvass.pack()

window.mainloop()