from tkinter import *

window = Tk()
window.title("My First GUI")
window.geometry('500x500')

# label = Label(window, text="Hello Tkinter")
# label.pack(fill=BOTH)

# def clicked():
#     label.configure(text="Text is changed after clicking on button...")

# btn = Button(window, text="Click Here...", fg="red", command=clicked)
# btn.pack()

label = Label(window, text="Hello ")
label.grid(column=1, row=0)

text_box = Entry(window, width=30)
text_box.grid(column=0, row=1)

def greet():
    text = text_box.get()
    label.configure(text="Hello " + text)

btn = Button(window, text="Click Here...", fg="red", command=greet)
btn.grid(column=1, row=1)

window.mainloop()