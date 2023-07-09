from tkinter import *

window=Tk()
window.geometry("500x500")
window.title("Python Programming")
window.configure(bg="red")

def hello():
    print("Button Clicked")


Button1=Button(window,text="OK",command=hello)
Button2=Button(window,text="OK",command=hello)

Button1.grid(row=0,column=0)
Button2.grid(row=1,column=0)


# Label=Label(window,text="Welcome")


# Button.pack()
# Button1.pack()
# Label.pack()


window.mainloop()