import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt
from celtic import *

def celtic_plot():
    n=int(row.get())
    m=int(col.get())
    matrix=full_generation(n,m)
    fig=plt.figure()
    im=plt.imshow(matrix,cmap="Greys")
    canvas= FigureCanvasTkAgg(fig,master=frame)
    canvas.draw()
    canvas.get_tk_widget().grid(row=5,column=0)

root= tk.Tk()
root.title("Celtic")
root.geometry("800x800")

frame = ttk.Frame(root,padding = 10)
frame.grid()

ttk.Label(frame,text="Celtic knot generator").grid()
ttk.Label(frame,text="Input row number (>=2)").grid(row=1,column=0)
ttk.Label(frame,text="Input column number (>=2)").grid(row=2,column=0)

row=tk.StringVar()
row_entry=tk.Entry(frame,textvariable=row)
row_entry.grid(row=1,column=1)
row_entry.insert(0,5)

col=tk.StringVar()
col_entry=tk.Entry(frame,textvariable=col)
col_entry.grid(row=2,column=1)
col_entry.insert(0,2)

ttk.Label(frame,text="Generate knot").grid(row=3,column=0)

generator_button = tk.Button(frame,command=celtic_plot,text="OK")
generator_button.grid(row=3,column=1)


    

root.mainloop()