from tkinter import *
root=Tk()

def myclick():
    mylabel=Label(root, text="button clicked !")
    mylabel.pack()
    
mybutton=Button(root, text="click me", padx=10 , pady=10 , command=myclick , fg="white" ,bg="#000000" )
mybutton.pack()
root.mainloop()

