from tkinter import *

window = Tk()
window.geometry("400x500")
window.title("Calculator")
window.configure(background="#3b403e")

def hello():
    print("Button Clicked")

button7=Button(window,text="7", bd=0, command=hello,width=7,height=1)
button4=Button(window,text="4", bd=0, command=hello,width=7,height=1)
button1=Button(window,text="1", bd=0, command=hello,width=7,height=1)
button0=Button(window,text="0", bd=0, command=hello,width=7,height=1)
button7.grid(row=-0,column=7)
button4.grid(row=1,column=7)
button1.grid(row=2,column=7)
button0.grid(row=3,column=7)

button8=Button(window,text="8",command=hello,width=7,height=1)
button8.grid(row=0,column=18)




window.mainloop()
print("hai")