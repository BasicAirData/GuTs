# Import the required libraries
from tkinter import *
from tkinter import ttk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
     FigureCanvasTkAgg)
import numpy as np
import pandas as pd

#Load data
dataset = pd.read_csv("20240825-095302 - Lago nero e rifugio segantini.txt")

# Create an instance of tkinter frame
win = Tk()
# Set the size of the tkinter window
win.geometry("600x1066")
win.title("GPS Logger Utils")
#win.configure(bg='#890000')
# Create an instance of ttk style
s = ttk.Style()
s.theme_use('default')
s.configure('TNotebook.Tab', font=('default', 15), padding=[125, 10], foreground='gray', background="#890000")
s.map("TNotebook.Tab",foreground=[("selected", "white")], background= [("selected", "#890000")])
nb = ttk.Notebook(win, style="TNotebook" )
f1= Frame(nb,background="light gray", width= 600, height=180)
nb.add(f1, text= 'Track')
f2 = Frame(nb,background="light gray", width= 600, height=180)
nb.add(f2, text= "Stats")
#Figure
fig, ax = plt.subplots()
# Create Canvas
canvas = FigureCanvasTkAgg(fig, f1)
canvas.get_tk_widget().grid(row = 2, column = 0)
# defining all 3 axis
z = dataset[['altitude(m)']]
x = dataset[['longitude']]
y = dataset[['latitude']]
 
# plotting
ax = plt.axes(projection ='3d')
ax.plot3D(x, y, z, 'green')
ax.set_title('Track plot')
canvas.draw()

#Header
Header= ttk.Frame(win)
Hlbl = Label(Header, text="GPS Logger Utils",fg='white', bg='#890000', font=("Default", 25))
Hlb2 = Label(Header, text="...",fg='white', bg='#890000', font=("Default", 25))
Hlb3 = Label(Header, text="                                               ",fg='#890000', bg='#890000', font=("Arial Bold", 25))
Hlbl.grid(column=0, row=0)
Hlb2.grid(column=2, row=0)
Hlb3.grid(column=1, row=0)
Header.columnconfigure(1, minsize=400)
#Footer
Footer= ttk.Frame(win, width= 600, height=180)
Flb1=Label(Footer, text="Load Track", font=("Default", 15))
Flb1.grid(column=0, row=0)
#Final layout
Header.pack()
nb.pack(expand= True, fill=BOTH, padx= 0, pady=0)
Footer.pack(padx= 5, pady=5)
win.mainloop()
