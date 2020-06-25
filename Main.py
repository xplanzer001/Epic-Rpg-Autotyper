import tkinter as tk
from tkinter import Text
import os
import pyautogui
import time
import threading
import keyboard
import threading

# Texts
huntText = "rpg hunt"
adventureText = "rpg adventure"
healText = "rpg heal"
fishText = "rpg net"
woodText = "rpg axe"

# Timers
huntTimer = 0
adventureTimer = 0
fishTimer = 0
woodTimer = 0

# Timer Indication
huntIsActive = True
adventureIsActive = True
fishIsActive = True
woodIsActive = True

# Quit Indication
yeetus = True

# Quit Button
def yeet():
    global yeetus
    yeetus = False

def heal():
    pyautogui.typewrite(healText)
    pyautogui.press('enter')
    time.sleep(1)

# Auto Hunt
def hunt():
    global huntIsActive
    global huntTimer

    pyautogui.typewrite(huntText)
    pyautogui.press('enter')
    huntIsActive = False
    huntTimer = time.time()
    time.sleep(1)

# Auto Adventure
def adventure():
    global adventureIsActive
    global adventureTimer

    pyautogui.typewrite(adventureText)
    pyautogui.press('enter')
    adventureIsActive = False
    adventureTimer = time.time()
    time.sleep(1)
    heal()

# Auto Wood
def wood():
    global woodIsActive
    global woodTimer

    pyautogui.typewrite(woodText)
    pyautogui.press('enter')
    woodIsActive = False
    woodTimer = time.time()
    time.sleep(1)

# Auto Fish
def fish():
    global fishIsActive
    global fishTimer

    pyautogui.typewrite(fishText)
    pyautogui.press('enter')
    fishIsActive = False
    fishTimer = time.time()
    time.sleep(1)

def reset():
    global huntTimer
    global adventureTimer
    global fishTimer
    global woodTimer
    global huntIsActive
    global adventureIsActive
    global fishIsActive
    global woodIsActive
    global yeetus

    # Timers
    huntTimer = 0
    adventureTimer = 0
    fishTimer = 0
    woodTimer = 0

    # Timer Indication
    huntIsActive = True
    adventureIsActive = True
    fishIsActive = True
    woodIsActive = True

    yeetus = True

def typer():
    global huntIsActive
    global adventureIsActive
    global woodIsActive

    time.sleep(3)
    while yeetus:
        print(yeetus)
        if huntIsActive and yeetus:
            hunt()
            
        if adventureIsActive and yeetus:
            adventure()

        if woodIsActive and yeetus:
            wood()

        if (time.time() - huntTimer > 123) and yeetus:
            huntIsActive = True

        if (time.time() - adventureTimer > 3603) and yeetus:
            adventureIsActive = True

        if (time.time() - woodTimer > 303) and yeetus:
            woodIsActive = True
    reset()

def start ():
    t1 = threading.Thread(target = typer)
    t1.start()

"""
def countdown(root, remaining = None):
        if remaining is not None:
            root.remaining = remaining

        if root.remaining <= 0:
            root.huntTime.configure(text="time's up!")
        else:
            root.huntTime.configure(text="%d" % root.remaining)
            root.remaining = root.remaining - 1
            root.after(1000, root.countdown)
"""

# Initialize Window
root = tk.Tk()

# Set Canvas
canvas = tk.Canvas(root, height = 300, width = 250, bg = "#263D42")
canvas.pack()

# Set Frame
frame = tk.Frame(root, bg = "white")
frame.place(relwidth = 0.9, relheight = 0.9, relx = 0.05, rely = 0.05)

# Title Text
title = tk.Label(frame, text = "EPIC RPG BOT", bg = "white", font = ("Helvetica", 20, "bold"))
title.pack()
title.place(relx = 0.5, rely = 0.3, anchor = "center")

# Timers
#huntTime = tk.Label(frame, text="", width=10)
#root.countdown(10)

# Run Button
start = tk.Button(frame, text = "Run", font = ("Helvetica", 20), padx = 15, pady = 5, fg = "white", bg = "#263D42", command = start)
start.pack()
start.place(relx = 0.24, rely = 0.7, anchor = "center")

# Stop Button
stop = tk.Button(frame, text = "Stop", font = ("Helvetica", 20), padx = 15, pady = 5, fg = "white", bg = "#cc1f1f", command = yeet)
stop.pack()
stop.place(relx = 0.74, rely = 0.7, anchor = "center")

# Lock Size
root.resizable(width=False, height=False)

# Display Window
root.mainloop()