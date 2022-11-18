# Written by AllTheSquares, program based off of this video: https://www.youtube.com/watch?v=QjWzjw6m20U

# Imports
import tkinter as tk
from PIL import Image, ImageSequence, ImageTk
import os # for shutdown command
from pygame import mixer # audio system

# Functions
def standing_mario(): # Swaps initial image of Mario kicking a hole through your screen to him standing asking for your liver
    global marioStand

    # Sets up the standing pose for Mario to be displayed after the kick is removed
    marioStand = tk.PhotoImage(file = 'Contents\marioStand.png') # Pulls image from contents folder
    marioStand = marioStand.zoom(2,2) # Enlargens image

    canvas.delete(Mario) # Deletes original instance of Mario (kicking pose)
    canvas.create_image(display_width/2,display_height/2, image = marioStand, anchor='center') # creates new canvas image at the same position of the original
    canvas.after(3500, hand_zoom)

def hand_zoom():
    global handFrame, handCanvas

    handCanvas = tk.Canvas(handFrame, width = display_width, height = display_height)
    handCanvas.pack()

    img = Image.open("Contents\hand.gif") 
    hand = tk.Label(handFrame) # Creates a label that will refresh per frame of the GIF.
    handCanvas.create_window(display_width/2.5, display_height/2.5, window = hand) # Places the GIF right near Mario's head as per the original meme video. 
    handFrame.attributes("-topmost", 'true')

    for img in ImageSequence.Iterator(img): # This for loop refreshes the gif for each frame (50)
        img = ImageTk.PhotoImage(img)
        hand.config(image = img)
        hand.update()
    
    # Functions to do after the zoom sequence ends: computer shutdown, audio stop
    handCanvas.after(0, shutdown_computer)
    handCanvas.after(0,mixer.music.stop)

def shutdown_computer():
    root.destroy()
    os.system("shutdown /s /t 0")

def start_anim(): # called by the original script (liver.py) after a random amount of time
    global root, canvas, hole, display_width, display_height, Mario, handFrame

    # Pygame Audio (plays the audio from the original video)
    mixer.init() 
    mixer.music.load("Contents\MarioLiver.wav")
    mixer.music.play(-1)


    # Sets up primary window of the "animation". This window will contain the hole in your screen that Mario creates after kicking through it.
    root = tk.Tk()
    display_width, display_height = root.winfo_screenwidth(), root.winfo_screenheight()
    root.attributes('-transparentcolor','#f0f0f0', "-topmost", 'true')
    root.geometry("%sx%s" % (display_width, display_height))
    root.overrideredirect(1)
    print(display_height, display_width)

    # This creates a toplevel window of the original Tkinter GUI instance used for the hole and Mario. This is for the gif of the hand zooming into your screen.
    handFrame = tk.Toplevel(root)
    handFrame.geometry("%sx%s" % (display_width, display_height))
    handFrame.attributes('-transparentcolor','#f0f0f0')
    
    handFrame.overrideredirect(1)

    # Specifies height and width of Canvas

    # Original source images found on the internet (made transparent with remove.bg)
    hole = tk.PhotoImage(file = "Contents\hole.png")
    marioKick = tk.PhotoImage(file = "Contents\marioKick.png")

    # Adds the hole image AND Mario himself
    canvas = tk.Canvas(root, width = root.winfo_screenwidth(), height = root.winfo_screenheight())
    canvas.create_image(display_width/2, display_height/2, image=hole, anchor = 'center')
    Mario = canvas.create_image(display_width/2, display_height/2, image=marioKick, anchor='center')
    canvas.pack(anchor="center")

    # Execute next function/next part of the "animation"
    canvas.after(1000, standing_mario)

    root.mainloop()

