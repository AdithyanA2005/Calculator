from tkinter import *

# Capturing click value and providing conditions

def click(event):
    global st_value
    text = event.widget.cget("text")
    print(text)

    if text=="=":
        if  st_value.get().isdigit():
            value = int(st_value.get())
        else:
            value = eval(screen.get())

        st_value.set(value)
        screen.update()


    elif text=="C":
         st_value.set("")
         screen.update()
    else:
        st_value.set(st_value.get() + text)
        screen.update()

# Create window and adding title and icon

window = Tk()
window.geometry("322x450")
window.title("ProditorNitro")
window.background="#000"
# window.wm_iconbitmap("")


# Creating a String to store the value and creating the display screen

st_value = StringVar()
st_value.set("")
screen = Entry(window, textvar=st_value, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

# Adding a frame creating three butttons
frame1 = Frame(window, background="#3b403e")

button = Button(frame1, text="9", padx=14, pady=9, font="lucida 35 bold")
button.pack(side=LEFT, padx=9, pady=3)
button.bind("<Button-1>", click)

button = Button(frame1, text="8", padx=14, pady=9, font="lucida 35 bold")
button.pack(side=LEFT, padx=9, pady=3)
button.bind("<Button-1>", click)

button = Button(frame1, text="7", padx=14, pady=9, font="lucida 35 bold")
button.pack(side=LEFT, padx=9, pady=3)
button.bind("<Button-1>", click)

button = Button(frame1, text="C", padx=14, pady=9, font="lucida 35 bold")
button.pack(side=LEFT, padx=9, pady=3)
button.bind("<Button-1>", click)


frame1.pack()
frame1 = Frame(window, background="#3b403e")


button = Button(frame1, text="6", padx=14, pady=9, font="lucida 35 bold")
button.pack(side=LEFT, padx=9, pady=3)
button.bind("<Button-1>", click)

button = Button(frame1, text="5", padx=14, pady=9, font="lucida 35 bold")
button.pack(side=LEFT, padx=9, pady=3 )
button.bind("<Button-1>", click)

button = Button(frame1, text="4", padx=14, pady=9, font="lucida 35 bold")
button.pack(side=LEFT, padx=9, pady=3)
button.bind("<Button-1>", click)

button = Button(frame1, text="=", padx=14, pady=, font="lucida 35 bold")
button.pack(side=LEFT, padx=9, pady=2)
button.bind("<Button-1>", click)


frame1.pack()
frame1 = Frame(window, background="#3b403e")


button = Button(frame1, text="3", padx=14, pady=9, font="lucida 35 bold")
button.pack(side=LEFT, padx=9, pady=3)
button.bind("<Button-1>", click)

button = Button(frame1, text="2", padx=14, pady=9, font="lucida 35 bold")
button.pack(side=LEFT, padx=9, pady=3)
button.bind("<Button-1>", click)

button = Button(frame1, text="1", padx=14, pady=9, font="lucida 35 bold")
button.pack(side=LEFT, padx=9, pady=3)
button.bind("<Button-1>", click)

button = Button(frame1, text="*", padx=14, pady=9, font="lucida 35 bold")
button.pack(side=LEFT, padx=9, pady=3)
button.bind("<Button-1>", click)


frame1.pack()
frame1 = Frame(window, background="#3b403e")

button = Button(frame1, text=".", padx=14, pady=9, font="lucida 35 bold")
button.pack(side=LEFT, padx=9, pady=3)
button.bind("<Button-1>", click)

button = Button(frame1, text="0", padx=18, pady=9, font="lucida 35 bold")
button.pack(side=LEFT, padx=9, pady=3)
button.bind("<Button-1>", click)

button = Button(frame1, text="+", padx=14, pady=9, font="lucida 35 bold")
button.pack(side=LEFT, padx=9, pady=3)
button.bind("<Button-1>", click)




frame1.pack()
frame1 = Frame(window, background="#3b403e")

button = Button(frame1, text="/", padx=14, pady=9, font="lucida 35 bold")
button.pack(side=LEFT, padx=9, pady=3)
button.bind("<Button-1>", click)

button = Button(frame1, text="%", padx=14, pady=9, font="lucida 35 bold")
button.pack(side=LEFT, padx=9, pady=3)
button.bind("<Button-1>", click)



button = Button(frame1, text="-", padx=14, pady=11, font="lucida 35 bold")
button.pack(side=LEFT, padx=9, pady=3)
button.bind("<Button-1>", click)

frame1.pack()
frame1 = Frame(window, background="#3b403e")







frame1.pack()

window.mainloop()
print("hai")
