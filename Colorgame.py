import tkinter as tk
import random as r
from tkinter import messagebox
colors=["Blue","Green","Red","Yellow","Orange","Grey",'Black','White','Indigo','Violet','Purple',"Brown"]
score=0
time_left=30
attempts=0
def game_start(event):
    if time_left==30:
        countdown()
    nextcolor()
def nextcolor():
    global score
    global time_left
    global attempts
    if time_left>0:
        attempts+=1
        e.focus_set()
        if e.get().lower()==colors[1].lower():
            score+=1
        e.delete(0,tk.END)    
        r.shuffle(colors)
        label.config(fg=str(colors[1]),text=str(colors[0]))
        scorelabel.config(text="SCORE"+str(score))
def countdown():
    global time_left,attempts
    if time_left>0:
        time_left-=1
        print(time_left)
        timelabel.config(text="Time left:"+str(time_left))
        root.after(1000,countdown)
    else:
        messagebox.showinfo("Game Over",f"Time Up you attempted {attempts} and {score} correct")       
root=tk.Tk()
root.title("Color game")
root.geometry("300x600")
ins=tk.Label(root,text="Type the word color ,not the word itself",font=("fixedsys",12))
ins.pack()
scorelabel=tk.Label(root,text="Please enter to start",font=("fixedsys",12))
scorelabel.pack()
timelabel=tk.Label(root,text="Time left:"+str(time_left),font=("fixedsys",12))
timelabel.pack()
label=tk.Label(root,font=("fixedsys",12))
label.pack()
e=tk.Entry(root)
root.bind("<Return>",game_start)
e.pack()
e.focus_set()
root.mainloop()

