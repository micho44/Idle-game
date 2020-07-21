import tkinter as tk
import time

def checkupgrade1():
    global upgrade
    with open("Points.txt", "r") as f:
        amount = int(f.read())
    with open("upgrade.txt", "r") as f:
        upgradejaki = int(f.read())
        if upgradejaki <= 1:
          if amount >= 100:
               with open("upgrade.txt", "w") as f:
                   f.write("2")
                   print("upgrade zmieniony")
               with open("Points.txt", "r") as f:
                   usun = int(f.read())
                   usun = usun - 100
                   print("Wartosc usun zmieniona")
               with open("Points.txt", "w") as f:
                  f.write(str(usun))
                  print("Nadpisanie uzywajac usun")
          else:
             tk.Label(upgrade, text="you dont have enough points").grid(row=3, columnspan=2)
        else:
            tk.Label(upgrade, text="You already have this upgrade").grid(row=3, columnspan=2)


def checkupgrade2():
    global upgrade
    with open("Points.txt", "r") as f:
        amount = int(f.read())
    with open("upgrade.txt", "r") as f:
        upgradejaki = int(f.read())
        if upgradejaki <= 4:
          if amount >= 1000:
               with open("upgrade.txt", "w") as f:
                   f.write("5")
                   print("upgrade zmieniony")
               with open("Points.txt", "r") as f:
                   usun = int(f.read())
                   usun = usun - 1000
                   print("Wartosc usun zmieniona")
               with open("Points.txt", "w") as f:
                  f.write(str(usun))
                  print("Nadpisanie uzywajac usun")
          else:
             tk.Label(upgrade, text="you dont have enough points").grid(row=3, columnspan=2)
        else:
            tk.Label(upgrade, text="You already have this upgrade").grid(row=3, columnspan=2)

def upgraderun():
    global upgrade
    upgrade = tk.Tk()
    upgrade.title("Upgrades!")
    upgrade.geometry('300x300')
    #adding exit button
    tk.Button(upgrade, text="Exit upgrade menu", fg="red",command=lambda :[upgrade.destroy()]).grid(row=2, columnspan=2)
    #making 1st upgrade (2 points per click)
    upgrade1 = tk.Button(upgrade, text="Buy me!", command=checkupgrade1)
    upgrade1.grid(row=0, column=1)
    tk.Label(upgrade, text="2 points per click-100points").grid(row=0, column=0)
    #making 2nd upgrade (5 points per click)
    upgrade2 = tk.Button(upgrade, text="Buy me!", command=checkupgrade2)
    upgrade2.grid(row=1, column=1)
    tk.Label(upgrade, text="5 points per click-1000points").grid(row=1, column=0)
    upgrade.mainloop()