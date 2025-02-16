'''
* Created by J.Larragueta on 06/02/2025
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
from tkinter import *
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
FigureCanvasTkAgg)
import numpy as np
import pandas as pd

dataset = pd.read_csv("20240825-095302 - Lago nero e rifugio segantini.txt")
class GuTs: # App class
        openFileName="N/A"
        def __init__(self, root):
            self.root = root
            self.root.title("GuTs - GPS Logger Utils")
            self.root.geometry("600x1066")
            center(root)
            self.root.resizable('FALSE','FALSE')
            #Load data from file, attention is fixed for test purposes :-)
            self.LoadTrack()
            #Notebook
            s = ttk.Style()
            s.theme_use('default')
            s.configure('TNotebook.Tab', font=('default', 15), padding=[125, 10], foreground='gray', background="#890000")
            s.map("TNotebook.Tab",foreground=[("selected", "white")], background= [("selected", "#890000")])
            self.setupHeader()
            self.notebook = ttk.Notebook(root, style="TNotebook")
            self.notebook.pack( fill='both')
            self.setupFooter()
            #Frame definition
            self.trackFrame = ttk.Frame(self.notebook)
            self.statsFrame = ttk.Frame(self.notebook)
            self.Header= ttk.Frame(self.root)

            self.trackFrame.pack(fill='both')
            self.statsFrame.pack(fill='both')
            #Adding tabs to notebook
            self.notebook.add(self.trackFrame, text='Track')
            self.notebook.add(self.statsFrame, text='Stats')
            #Setup grafic elements for each tab
            self.setupTrackTab()
            self.setupStatsTab()
        def setupHeader (self):  #Setup the header
            Header= ttk.Frame(self.root)
            Hlbl = Label(Header, text="GPS Logger Utils",fg='white', bg='#890000', font=("Default", 25))
            Hlb2 = Label(Header, text="...",fg='white', bg='#890000', font=("Default", 25))
            Hlb3 = Label(Header, text="                                               ",fg='#890000', bg='#890000', font=("Arial Bold", 25))
            Hlbl.grid(column=0, row=0)
            Hlb2.grid(column=2, row=0)
            Hlb3.grid(column=1, row=0)
            Header.columnconfigure(1, minsize=400)
            Header.pack(fill='both')
        
        def setupTrackTab(self):  #Setup the track tab       
            self.label = ttk.Label(self.trackFrame, text=self.openFileName)
            self.label.pack(pady=10)
            #Figure
            self.fig, self.ax = plt.subplots()
            # Create Canvas
            self.canvas = FigureCanvasTkAgg(self.fig, self.trackFrame)
            self.canvas.get_tk_widget().pack(fill='both')
            # defining all 3 axis, calculate basic stats
            self.z = dataset[['altitude(m)']]
            self.x = dataset[['longitude']]
            self.y = dataset[['latitude']]
            nsamples=self.z.count 
            # plotting
            ax = plt.axes(projection ='3d')
            ax.plot3D(self.x, self.y, self.z, 'green')
            ax.set_title('Track plot')
            self.canvas.draw()
            #Initial point selection
            self.slider1var = IntVar()
            self.slider1 = Scale(self.trackFrame, from_=1, to=10, orient='horizontal')
            self.slider1.pack()
            self.slider1['variable'] = self.slider1var
            self.slider1['command'] = self.update
        def setupStatsTab(self):
            self.statsLabel = ttk.Label(self.statsFrame, text="Statistics will be displayed here.")
            self.statsLabel.pack(pady=10)
        def setupFooter(self): #Setup footer
            Footer= ttk.Frame(self.root, width= 600, height=180)
            Flb1=Label(Footer, text="Load Track", font=("Default", 15))
            Flb1.grid(column=0, row=0)
            Footer.pack(padx= 5, pady=5,fill='both')
        def update(self, event):
            #Need conversione between panda list and numpy is needed
            #print(self.slider1.get())
            inda=self.slider1.get()
            self.ax.plot(inda,inda,inda , marker='x' , markersize=200, markeredgecolor="green", markerfacecolor="red")
            self.canvas.draw()
 
        def LoadTrack(self):
            self.openFileName = "GPS track 123456789 123456789"
#Centers a windows on the screen
def center(window): 
        window.update_idletasks()
        width = window.winfo_width()
        height = window.winfo_height()
        screenWidth = window.winfo_screenwidth()
        screenHeight = window.winfo_screenheight()
        x = (screenWidth - width) // 2
        y = (screenHeight - height) // 2
        window.geometry(f"{width}x{height}+{x}+{y}")
            
if __name__ == "__main__":
    root = Tk()
    app = GuTs(root)
    root.mainloop()
