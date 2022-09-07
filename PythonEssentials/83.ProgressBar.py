from tkinter import *
from tkinter.ttk import *
import time

def start():
    #   tasks = 10
    GB = 50
    #   x = 0
    download = 0
    speed = 1
    # while x < tasks:
    while download < GB:
        time.sleep(0.05)
        #   bar['value'] += 10
        bar['value'] += (speed/GB) * 100
        download += speed # 1 is the old value
        # percent.set(str(int((x/tasks)*100)) + "%")
        # text.set(str(x) + "/" + str(tasks) + "tasks completed")
        percent.set(str(int((download / GB) * 100)) + "%")
        text.set(str(download) + "/" + str(GB) + " tasks completed")
        window.update_idletasks()   # update the progress bar every iteration

    if bar['value'] == 100:
        time.sleep(1)
        window.destroy()

window = Tk()

percent = StringVar()
text = StringVar()

bar = Progressbar(window, orient=HORIZONTAL, length=300)
bar.pack(pady=10)

percent_label = Label(window, textvariable=percent).pack()
task_label = Label(window, textvariable=text).pack()

button = Button(window, text="download", command=start).pack()

window.mainloop()
