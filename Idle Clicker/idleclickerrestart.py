import tkinter as tk

def restart():
    global restart
    restart = tk.Tk()
    restart.config(bg="#e35959")
    #label
    tk.Label(restart, text="You want to restart your progress?", bg="#e35959").grid(row=0, columnspan=2)
    #buttons
    yesbtn = tk.Button(restart, text="Yes", fg="dark red", bg="red", command=yescommand).grid(row=1, column=0)
    nobtn = tk.Button(restart, text='no', fg="dark green", bg="#51f542", command=nocommand).grid(row=1, column=1)

    restart.mainloop()

def yescommand():
    global restart
    with open("Points.txt", "w") as f:
        f.write("0")
    with open("upgrade.txt", "w") as f:
        f.write("1")
    restart.destroy()

def nocommand():
    global restart
    restart.destroy()