import numpy as np
import cv2
import tkinter 
from PIL import Image, ImageTk

# Load an color image
img = cv2.imread('img.png')

#Rearrang the color channel
b,g,r = cv2.split(img)
img = cv2.merge((r,g,b))

# A root window for displaying objects
root = Tkinter.Tk()  

# Convert the Image object into a TkPhoto object
im = Image.fromarray(img)
imgtk = ImageTk.PhotoImage(image=im) 

# Put it in the display window
Tkinter.Label(root, image=imgtk).pack() 

root.mainloop() # Start the GUI