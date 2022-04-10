from PIL import Image
import cv2
from scipy.signal import find_peaks
import numpy as np

#Function to calculate the red portion in a pixel
#Returns the average red in each frame
def r_of_img(img):
    sumr=0
    im = Image.open(img).convert('RGB')
    width, height = Image.open(img).size
    for x in range(1,width):
        for y in range(1,height):
            r, g, b = im.getpixel((x, y))
            sumr+=r
    return (sumr/(x*y))

vidcap = cv2.VideoCapture("Path of Test Video")
success,image = vidcap.read()
count = 0
val=[]

#Loop to convert Video into frames,
#calculate the red part in each pixel
#produces an array conatining values against each frame as output
while count<300:
    cv2.imwrite("Path of Temp Folder\frame%d.jpg" % count, image) 
    success,image = vidcap.read()
    img = ("Path of Temp Folder\frame%d.jpg" % count)
    val.append(r_of_img(img))
    count += 1

peaks, _ = find_peaks(val,distance=15) #Peak Identification
a=np.diff(peaks)                       #Calculate distance between 2 peaks
avg=sum(a)/len(a)                      
HR=round((60/avg)*30)                  #Calculate Heart Rate

#Displaying the Heart Rate as an Info pop-up
from tkinter import *
import tkinter.messagebox
disp = tkinter.Tk()
tkinter.messagebox.showinfo("Info","Your Heart Rate is %d bpm" %HR)
mainloop()
