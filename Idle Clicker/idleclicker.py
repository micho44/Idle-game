import time
import tkinter as tk
from idleclickerupgrades import *
from idleclickerrestart import *
with open("Points.txt", "r") as f:
    points = int(f.read())

with open("upgrade.txt", "r") as f:
    upgrade = int(f.read())
#saving points
def clickfun():
    global points
    points = points + int(upgrade)
    with open("Points.txt", "w") as f:
        f.write(str(points))
#updating point counter
def update():
    global wynik, punkty
    wynik = tk.Label(main, text="", bg="dark gray")
    wynik.grid(row=2, column=1)
    with open("Points.txt", "r") as f:
       punkty = f.read()
       wynik.config(text=" You have :" + punkty + " points.")

def refresh():
    global upgrade, points
    with open("upgrade.txt", "r") as f:
        upgrade = int(f.read())
    with open("Points.txt", "r") as f:
        points = int(f.read())

def exit():
    main.destroy()
#creating window
main = tk.Tk()
#setting up window config
main.config(bg="dark gray")
main.title("Idle clicker")
main.geometry('150x150')
#Making click button
click = tk.Button(main, text="Click me to gain points", bg="light blue", command=lambda:[refresh(), clickfun(), update()])
click.grid(row=0, column=1)
#making labels
tk.Label(main, text="You get " + str(upgrade) + " points per click", bg="dark gray").grid(row=1, column=1)
#upgrade button
upgrades = tk.Button(main, text="Upgrades", bg="gray", command=upgraderun)
upgrades.grid(row=3, column=1)
#exit and restart button
#exit
exitbtn = tk.Button(main, text="Exit", bg="light gray", command=exit)
exitbtn.grid(row=4, column=1)
#restart
restartbtn = tk.Button(main,text="Restart progress", bg="black", fg="white", command=restart)
restartbtn.grid(row=5, column=1)
main.mainloop()