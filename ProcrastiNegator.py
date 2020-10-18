"""ProcrastiNegator."""

from tkinter import *
import winsound
from typing import List


# click functions for add and remove task buttons
def click():
    entered_text = textentry.get()
    output.delete(0.0, END)
    tasks.append(entered_text)
    output.insert(END, tasks)

def click2():
    entered_text = textentry2.get()
    entered_text = int(entered_text)
    output.delete(0.0, END)
    tasks.pop(entered_text - 1)

    output.insert(END, tasks)

# functions for set timer and start timer buttons
time0 = 0

def set_timer():
    global time0
    hour = input_hours.get()
    hour = int(hour)
    minute = input_minutes.get()
    minute = int(minute)
    second = input_seconds.get()
    second = int(second)
    time0 += hour*3600 + minute*60 + second
    new_time = str(hour) + ':' + str(minute) + ':' + str(second)
    timer.config(text=new_time)
    return time0

def countdown():
    global time0
    if time0 > 0:
        seconds = (time0 % 60)
        minutes = (time0 // 60) % 60
        hours = (time0 // 3600)
        new_time = str(hours) + ':' + str(minutes) + ':' + str(seconds)
        timer.config(text=new_time)
        time0 -= 1
        timer.after(1000,countdown)
    elif time0 == 0:
        timer.config(text="TIME'S UP!!!")
        winsound.PlaySound("alarm_sound", winsound.SND_FILENAME)

# creating the window
window = Tk()
window.title("ProcrastiNegator")
window.configure(background="lightblue")

# title
Label(window, text="ProcrastiNegator", bg="lightblue", fg="royalblue", font="Arial 30 bold") .grid(row=1, column=0, sticky=W)
Label(window, text="Let's Negate your Procrastination!!!\n", bg="lightblue", fg="royalblue", font="Arial 14") .grid(row=2, column=0, sticky=W)

# text entry box for adding task
textentry = Entry(window, width=30, bg="white")
textentry.grid(row=3, column=0, stick=W)
Button(window, text="ADD TASK", width=8, command=click).grid(row=4, column=0, sticky=W)

# text entry box for removal of task
textentry2 = Entry(window, width=30, bg="white")
textentry2.grid(row=5, column=0, stick=W)
Button(window, text="REMOVE TASK", width=11, command=click2).grid(row=6, column=0, sticky=W)

# Output of Tasks
Label(window, text="\nTasks:", bg="lightblue", fg="royalblue", font="Arial 12 bold").grid(row=7, column=0, sticky=W)
output = Text(window, width=75, height=6, wrap=WORD, background="white")
output.grid(row=8, column=0, columnspan=2, sticky=W)


# hours
Label(window, text="\nHours", bg="lightblue", fg="royalblue", font="Arial 12").grid(row=9, column=0, sticky=W)
input_hours = Entry(window, width=30, bg="white")
input_hours.grid(row=10, column=0, stick=W)
# minutes
Label(window, text="Minutes", bg="lightblue", fg="royalblue", font="Arial 12").grid(row=11, column=0, sticky=W)
input_minutes = Entry(window, width=30, bg="white")
input_minutes.grid(row=12, column=0, stick=W)
# seconds
Label(window, text="Seconds", bg="lightblue", fg="royalblue", font="Arial 12").grid(row=13, column=0, sticky=W)
input_seconds = Entry(window, width=30, bg="white")
input_seconds.grid(row=14, column=0, stick=W)

# add time button button
Button(window, text="SET TIMER", width=15, command=set_timer).grid(row=15, column=0, sticky=W)
Button(window, text="START TIMER", width=15, command=countdown).grid(row=16, column=0, sticky=W)


# Timer
Label(window, text="\nTimer:", bg="lightblue", fg="royalblue", font="Arial 12 bold").grid(row=17, column=0, sticky=W)
timer = Label(window, bg="lightblue", fg="royalblue", font="Arial 30 bold")
timer.grid(row=18, column=0, sticky=W)

# the dictionary for the list of tasks
tasks: List[str] = []

# exit function
def close_window():
    window.destroy()
    exit()

# exit button
Button(window, text="EXIT", width=14, command=close_window).grid(row=19, column=0, sticky=W)

window.mainloop()