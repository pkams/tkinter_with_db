# Importing Lib
from tkinter import *

# Creating Window Object
window = Tk()

# Definying labels: title, author, year ISBM
l1 = Label(window, text="Title")
l1.grid(row=0, column=0)
l2 = Label(window, text="Author")
l2.grid(row=0, column=2)
l3 = Label(window, text="Year")
l3.grid(row=1, column=0)
l4 = Label(window, text="ISBM")
l4.grid(row=1, column=2)

# Main loop where all window objects will be declared
window.mainloop()