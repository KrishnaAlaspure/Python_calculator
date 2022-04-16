from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("Images")
root.iconbitmap('E:/Tkinter/icon.ico')

def forw(img_number):
    global my_label
    global for_button
    global back_button
    return

def back():
    return

my_img1=ImageTk.PhotoImage(Image.open("E:/Tkinter/Images/i1.jpg"))
my_img2=ImageTk.PhotoImage(Image.open("E:/Tkinter/Images/i2.jpg"))
my_img3=ImageTk.PhotoImage(Image.open("E:/Tkinter/Images/i3.jpg"))
my_img4=ImageTk.PhotoImage(Image.open("E:/Tkinter/Images/i4.jpg"))
my_img5=ImageTk.PhotoImage(Image.open("E:/Tkinter/Images/i5.jfif"))
my_img6=ImageTk.PhotoImage(Image.open("E:/Tkinter/Images/i6.jpg"))
my_img7=ImageTk.PhotoImage(Image.open("E:/Tkinter/Images/i7.jfif"))

img_list=[my_img1,my_img2,my_img3,my_img4,my_img5,my_img6,my_img7 ]
my_label=Label(image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)

back_button=Button(root,text="Back",command=back())
exit_button=Button(root,text="Exit",command=root.)
for_button=Button(root,text="Forward",command=lambda:forw(2))

back_button.grid(row=1,column=0)
exit_button.grid(row=1,column=1)
for_button.grid(row=1,column=2)
root.mainloop()

