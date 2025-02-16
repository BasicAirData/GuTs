'''
* Created by J.Larragueta on 04/02/2025
 * This file is part of BasicAirData GPS Logger Utils
 *
 * Copyright (C) 2011 BasicAirData
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program. If not, see <http://www.gnu.org/licenses/>.
 */
'''
#It is necessary to redo the skeleton in a class oriented mode

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

class main:
    def __init__(self, parent):
        #self.label1 =Label(parent,text="Initial")
        #self.label1.pack()
        #madness begin here
        #Configure Notebook
        s = ttk.Style()
        s.theme_use('default')
        s.configure('TNotebook.Tab', font=('default', 15), padding=[125, 10], foreground='gray', background="#890000")
        s.map("TNotebook.Tab",foreground=[("selected", "white")], background= [("selected", "#890000")])
        self.nb = ttk.Notebook(parent, style="TNotebook" )
        self.f1= Frame(self.nb,background="light gray", width= 600, height=180)
        self.nb.add(self.f1, text= 'Track')
        #Track tabs
        #Figure
        self.fig, self.ax = plt.subplots()
        # Create Canvas
        self.canvas = FigureCanvasTkAgg(self.fig, self.f1)
        self.canvas.get_tk_widget().grid(row = 0, column = 0)
        # defining all 3 axis, calculate basic stats
        self.z = dataset[['altitude(m)']]
        self.x = dataset[['longitude']]
        self.y = dataset[['latitude']]

        nsamples=self.z.count 
        # plotting
        self.ax = plt.axes(projection ='3d')
        self.ax.plot3D(self.x, self.y, self.z, 'green')
        self.ax.set_title('Track plot')
        self.canvas.draw()
        #Initial point selection
        self.slider1var = IntVar()
        self.slider1 = Scale(self.f1, from_=1, to=10, orient='horizontal')
        self.slider1.grid(row=1,column=0)
        self.slider1['variable'] = self.slider1var
        #Header
        self.Header= ttk.Frame(parent)
        self.Hlbl = Label(self.Header, text="GPS Logger Utils",fg='white', bg='#890000', font=("Default", 25))
        self.Hlb2 = Label(self.Header, text="...",fg='white', bg='#890000', font=("Default", 25))
        self.Hlb3 = Label(self.Header, text="                                               ",fg='#890000', bg='#890000', font=("Arial Bold", 25))
        self.Hlbl.grid(column=0, row=0)
        self.Hlb2.grid(column=2, row=0)
        self.Hlb3.grid(column=1, row=0)
        self.Header.columnconfigure(1, minsize=400)
        self.Header.pack()
        self.nb.pack(expand= True, fill=BOTH, padx= 0, pady=0) 
class ctrl:
    def __init__(self, window, dataset):
        self.window = window
        self.window.slider1['command'] = self.update
        self.datain=dataset
    def update(self, event):
        #Init pointer
     #   z = self.datain[['altitude(m)']]
     #   x = self.datain[['longitude']]
     #   y = self.datain[['latitude']]
        #self.window.ax.plot(x[1],y[1] ,z[1] , marker='x' , markersize=200, markeredgecolor="green", markerfacecolor="red")
        print(x[0])
        
if __name__ == '__main__':
    root = Tk()
    
    ctrl(main(root),dataset)
    root.geometry("600x1066")
    root.resizable(False,False)
    root.title("GPS Logger Utils")
    root.mainloop()