from tkinter import *

# Capturing click value and providing conditions

def click(event):
    global st_value
    text = event.widget.cget("text")
    print(text)

    if text=="=":
        pass
    elif text == "C":
        pass

    else:
        st_value.set(st_value.get() + text)
        screen.update()

# Create window and adding title and icon

window = Tk()
window.geometry("322x450")
window.title("ProditorNitro")
# window.wm_iconbitmap("")


# Creating a String to store the value and creating the display screen

st_value = StringVar()
st_value.set("")
screen = Entry(window, textvar=st_value, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

# Adding a frame creating three butttons
frame1 = Frame(window, background="#3b403e")

button = Button(frame1, text="9", padx=14, pady=11, font="lucida 35 bold")
button.pack(side=LEFT, padx=9, pady=6)
button.bind("<Button-1>", click)

button = Button(frame1, text="8", padx=14, pady=11, font="lucida 35 bold")
button.pack(side=LEFT, padx=9, pady=6)
button.bind("<Button-1>", click)

button = Button(frame1, text="7", padx=14, pady=11, font="lucida 35 bold")
button.pack(side=LEFT, padx=9, pady=6)
button.bind("<Button-1>", click)

frame1.pack()

window.mainloop()
print("hai")
