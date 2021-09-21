# Importing Lib
from tkinter import *
import backend

# Creating Window Object
window = Tk()

# Starting backend
backend.connect()

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

# 3. Define Listbox
listbox = Listbox(window, height=6, width=35,)
listbox.grid(row=2, column=0, rowspan = 6, columnspan=2)

# 3.1 Attaching scrollbar
scroll = Scrollbar(window)
scroll.grid(row=2, column=2, rowspan=6)

listbox.configure(yscrollcommand=scroll.set)
scroll.configure(command=listbox.yview)

# 4. Define buttons
b1 = Button(window, text='View All', width=12, command = lambda: backend.view())
b1.grid(row=2, column=3)

b2 = Button(window, text='Search Entry', width=12, command=lambda: backend.search(title=title_text.get(),
                                                                                  author=author_text.get(),
                                                                                  year=year_text.get(),
                                                                                  isbm=isbm_text.get()))
b2.grid(row=3, column=3)

b3 = Button(window, text='Add Entry', width=12, command=lambda: backend.insert(title=title_text.get(),
                                                                                  author=author_text.get(),
                                                                                  year=year_text.get(),
                                                                                  isbm=isbm_text.get()))
b3.grid(row=4, column=3)

b4 = Button(window, text='Update selected', width=12, command=lambda: backend.update(id = 0,title=title_text.get(),
                                                                                  author=author_text.get(),
                                                                                  year=year_text.get(),
                                                                                  isbm=isbm_text.get()))
b4.grid(row=5, column=3)
b5 = Button(window, text='Deleted selected', width=12, command=lambda: backend.delete(id=0))
b5.grid(row=6, column=3)
b6 = Button(window, text='Close', width=12)
b6.grid(row=6, column=3)


# Main loop where all window objects will be declared
window.mainloop()