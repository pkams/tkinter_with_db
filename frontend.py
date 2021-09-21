# Importing Lib
from tkinter import *

# Creating Window Object
window = Tk()

# 1.Define labels
l1 = Label(window, text="Title")
l1.grid(row=0, column=0)
l2 = Label(window, text="Author")
l2.grid(row=0, column=2)
l3 = Label(window, text="Year")
l3.grid(row=1, column=0)
l4 = Label(window, text="ISBM")
l4.grid(row=1, column=2)

# 2. Define Entries
title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)
author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)
year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)
isbm_text = StringVar()
e4 = Entry(window, textvariable=isbm_text)
e4.grid(row=1, column=3)

# Main loop where all window objects will be declared
window.mainloop()