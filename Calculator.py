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
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value="error"


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
window.geometry("320x450")
window.title("ProditorNitro")
window.background="#000"
# window.wm_iconbitmap("")


# Creating a String to store the value and creating the display screen

st_value = StringVar()
st_value.set("")
screen = Entry(window, textvar=st_value, bg="#38c7b9", fg="#032d30", font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

# Adding a frame creating three butttons
frame1 = Frame(window, background="#2f524e")

button = Button(frame1, text="9", padx=14, pady=9, font="lucida 35 bold")
button.pack(side=LEFT, padx=9, pady=3)
button.bind("<Button-1>", click)

button = Button(frame1, text="8", padx=14, pady=9, font="lucida 35 bold")
button.pack(side=LEFT, padx=9, pady=3)
button.bind("<Button-1>", click)

button = Button(frame1, text="7", padx=14, pady=9, font="lucida 35 bold")
button.pack(side=LEFT, padx=9, pady=3)
button.bind("<Button-1>", click)

button = Button(frame1, text="AC", padx=14, pady=9, font="lucida 35 bold")
button.pack(side=LEFT, padx=9, pady=3)
button.bind("<Button-1>", click)


frame1.pack()
frame1 = Frame(window, background="#2f524e")


button = Button(frame1, text="6", padx=14, pady=9, font="lucida 35 bold")
button.pack(side=LEFT, padx=9, pady=3)
button.bind("<Button-1>", click)

button = Button(frame1, text="5", padx=14, pady=9, font="lucida 35 bold")
button.pack(side=LEFT, padx=9, pady=3 )
button.bind("<Button-1>", click)

button = Button(frame1, text="4", padx=14, pady=9, font="lucida 35 bold")
button.pack(side=LEFT, padx=9, pady=3)
button.bind("<Button-1>", click)

button = Button(frame1, text="=", padx=14, pady=9, font="lucida 35 bold")
button.pack(side=LEFT, padx=9, pady=2)
button.bind("<Button-1>", click)


frame1.pack()
frame1 = Frame(window, background="#2f524e")


button = Button(frame1, text="3", padx=14, pady=9, font="lucida 35 bold")
button.pack(side=LEFT, padx=9, pady=3)
button.bind("<Button-1>", click)

button = Button(frame1, text="2", padx=14, pady=9, font="lucida 35 bold")
button.pack(side=LEFT, padx=9, pady=3)
button.bind("<Button-1>", click)

button = Button(frame1, text="1", padx=14, pady=9, font="lucida 35 bold")
button.pack(side=LEFT, padx=9, pady=3)
button.bind("<Button-1>", click)

button = Button(frame1, text="+", padx=14, pady=9, font="lucida 35 bold")
button.pack(side=LEFT, padx=9, pady=3)
button.bind("<Button-1>", click)


frame1.pack()
frame1 = Frame(window, background="#2f524e")


button = Button(frame1, text=".", padx=21, pady=10, font="lucida 35 bold")
button.pack(side=LEFT, padx=9, pady=3)
button.bind("<Button-1>", click)

button = Button(frame1, text="0", padx=14, pady=9, font="lucida 35 bold")
button.pack(side=LEFT, padx=9, pady=3)
button.bind("<Button-1>", click)

button = Button(frame1, text="*", padx=17, pady=9, font="lucida 35 bold")
button.pack(side=LEFT, padx=9, pady=3)
button.bind("<Button-1>", click)

button = Button(frame1, text="%", padx=14, pady=9, font="lucida 35 bold")
button.pack(side=LEFT, padx=9, pady=3)
button.bind("<Button-1>", click)


frame1.pack()
frame1 = Frame(window, background="#2f524e")


button = Button(frame1, text="/", padx=14, pady=9, font="lucida 35 bold")
button.pack(side=LEFT, padx=9, pady=3)
button.bind("<Button-1>", click)

button = Button(frame1, text="-", padx=14, pady=11, font="lucida 35 bold")
button.pack(side=LEFT, padx=9, pady=3)
button.bind("<Button-1>", click)

frame1.pack()
window.configure(bg="#2f524e")
window.mainloop()
print("hai")
