# Written by AllTheSquares, based off of this image/video: https://www.youtube.com/watch?v=EXGDoH4SDR0
# imports
import tkinter as tk
import tkinter.messagebox as msg
import marioLiverAnim as anim
import time
import random

# functions
def ok_command(): # executes the animation script
    root.destroy()
    deathClock = random.randint(0,60) # Randomizes time before execution from 0 to 60 sec
    print(deathClock)
    time.sleep(deathClock)
    anim.start_anim()

def disable_close(): #disables Close Window button
   pass

def cancel_command(): # Function that destroys the cancel button when clicked
    msg.showerror("Error", "THAT IS NOT AN OPTION.")
    Cancel_Button.destroy()

def mario_error(): # creates the error GUI 
    # creates windows-esque popup
    canvas.create_rectangle(0, 0, 300, 125, fill='white')
    canvas.create_rectangle(0, 85, 300, 125, fill='lightgray', outline = "lightgray")

    # adds mario image and elements of the program (the buttons, message)
    canvas.create_image(10,10, anchor = tk.NW, image=mario)
    canvas.create_window(270, 35, anchor= tk.NE, window=threat)
    canvas.create_window(210, buttonY, anchor= tk.SE, window=okbutton)
    canvas.create_window(290, buttonY, anchor= tk.SE, window=Cancel_Button)

    root.protocol("WM_DELETE_WINDOW", disable_close) # Calls function to disable Close Window Button
    canvas.pack()

# setup main window
root = tk.Tk()
root.eval('tk::PlaceWindow . center')
root.geometry("300x125")
root.resizable(False, False)
root.title("")
root.iconbitmap('./Contents/mario.ico')

canvas = tk.Canvas(root, width = 300, height = 125)

# tkinter widget setup + mario png variable
threat = tk.Label(root, text = "3 Days until Mario steals your liver!", bg="white")
okbutton = tk.Button(root, text="       OK       ", command = ok_command)
Cancel_Button = tk.Button(root, text="    Cancel    ",command = cancel_command)
mario = tk.PhotoImage(file = "./Contents/marioHead.png")

buttonY = 118

mario_error()

root.mainloop()