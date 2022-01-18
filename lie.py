
from tkinter import *
 
root = Tk()
 
 
 
TL = Label(root, text="Top Left", bg="pale turquoise")
TL.grid(row =1, column = 0)
 
TM= Button(root, text="Top Middle", bg="White")
TM.grid( row =1, column = 1)
 
TR  = Button(root, text="Top Right", bg="turquoise")
TR.grid( row =1, column = 2,)
 
ML = Button(root, text="Middle Left", bg="grey")
ML.grid( row =2, column = 0)
 
MMa = Button(root, text="MiddelMiddleA", bg="yellow")
MMa.grid( row =2, column = 1)
 
MMb = Button(root, text="MiddleMiddleb", bg="yellow")
MMb.grid( row =2, column = 2)
 
MMc = Button(root, text="MiddleMiddlec", bg="yellow")
MMc.grid(row =2, column = 3)
 
MMd = Button(root, text="MiddleMiddled", bg="yellow")
MMd.grid( row =2, column = 4)
 
MMe = Button(root, text="MiddleMiddlee", bg="yellow")
MMe.grid( row =2, column = 5)
 
BottomLeft = Button(root, text="BottomLeft", bg="deep pink")
BottomLeft.grid( row =3, column = 0)
 
BottomRight = Button(root, text="BottomRight", bg="red")
BottomRight.grid( row =3, column = 1)
 
 
 
root.mainloop()