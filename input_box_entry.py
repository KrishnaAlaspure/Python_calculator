from tkinter import *
root=Tk()

e=Entry(root , width=50 ,bg="white", fg="red" ,borderwidth=5)
e.pack()
e.insert(0, "Enter your name")
def myclick():
    hello="hello "+e.get()
    mylabel=Label(root, text=hello)
    mylabel.pack()
     
mybutton=Button(root, text="click", padx=10 , pady=10 , command=myclick , fg="white" ,bg="#000000" )
mybutton.pack()
root.mainloop()

