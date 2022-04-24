from tkinter import *
import tkinter.font as font

window = Tk()
window.title("My First GUI")
window.geometry('500x500')

expression = StringVar()
customFont = font.Font(size=20)

label = Label(window, text="Hello world...", font=(customFont), fg='white', bg='black')
# grid
# label.grid(row=0, column=0, padx=10, pady=10)

label_2 = Label(window, text="This is some text", font=(customFont))
# label_2.grid(row=0, column=1)

# pack
label.pack(fill=BOTH)
# label_2.pack(fill=BOTH)

# label.pack(fill=BOTH, side=LEFT)
# label_2.pack(fill=BOTH, side=LEFT)

# place
# label.place(x = 10, y = 20)
label_2.place(x = 150, y = 100)

window.mainloop()