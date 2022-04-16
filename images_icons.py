from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("Images")
root.iconbitmap('E:/Tkinter/icon.ico')
button_quit=Button(root, text="exit",command=root.quit).pack ()
my_img=ImageTk.PhotoImage(Image.open("i1.jpg"))
my_label=Label(image=my_img)
my_label.pack()

root.mainloop()

