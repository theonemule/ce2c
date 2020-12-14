import tkinter as tk
 
# Create the master object
master = tk.Tk()
 
# Labels for the entry boxes
tk.Label(master, text="Value 1:").grid(row=0, column=0)
tk.Label(master, text="Value 2:").grid(row=1, column=0)
tk.Label(master, text="Result:").grid(row=5, column=0)
 
# sets up some "entry" boxes for input
e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
 
# adds the entries to the grid
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=5, column=1)

def add():
    val1 = float(e1.get())
    val2 = float(e2.get())
    val3 = val1 + val2
    e3.delete(0,100)
    e3.insert(0, str(val3))

def sub():
    val1 = float(e1.get())
    val2 = float(e2.get())
    val3 = val1 - val2
    e3.delete(0,100)
    e3.insert(0, str(val3))

def mul():
    val1 = float(e1.get())
    val2 = float(e2.get())
    val3 = val1 * val2
    e3.delete(0,100)
    e3.insert(0, str(val3))

def div():
    val1 = float(e1.get())
    val2 = float(e2.get())
    val3 = val1 / val2
    e3.delete(0,100)
    e3.insert(0, str(val3))

# sets up the buttons
addBtn = tk.Button(master, text="+", command=add)
addBtn.grid(row=3, column=0)
subBtn = tk.Button(master, text="-", command=sub)
subBtn.grid(row=3, column=1)
mltBtn = tk.Button(master, text="x", command=mul)
mltBtn.grid(row=4, column=0)
divBtn = tk.Button(master, text="÷", command=div)
divBtn.grid(row=4, column=1)

# main is needed to keep the app up
tk.mainloop()