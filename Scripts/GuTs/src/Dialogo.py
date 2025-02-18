from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import pandas as pd
#Select file and load data
class Dialogo:
    def __init__(self,initialdir):
        self.data=pd.DataFrame()
        self.initialdir=initialdir
        self.filename=''
    def openFile(self):   #Dialog box + read data
        try:
            #here you open the file
            filetypes = (('GPS Logger text files', '*.txt'),('All files', '*.*'))
            filename = fd.askopenfilename(title='Open a GPS Logger file',initialdir=self.initialdir ,filetypes=filetypes)
            self.data = pd.read_csv(filename)
            self.filename=filename
        except:
            showinfo(title='Error!', message='Select only GPS Logger files')
        finally:  #here we close the file anyway
            pass