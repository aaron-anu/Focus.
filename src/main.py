import os
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as m
import pandas as pd

from lib import tasks

# Specify custom data directory. By default ../data/
data_dir=None


def main(data_dir):

    # create data dir
    if data_dir == None:
        data_dir = os.path.dirname(os.path.abspath(__file__)) + "/../data"
    if not os.path.exists(data_dir):
        os.mkdir(data_dir)
    tasksFilePath=data_dir+'/tasks.csv'
    
    if os.path.exists(tasksFilePath):
        tasksDataframe=pd.read_csv(tasksFilePath)
    else:
        tasksDataframe = pd.DataFrame()
        tasksDataframe.to_csv(tasksFilePath, index=False)
    
    # Initialize tkinter
    root = tk.Tk()
    root.geometry('720x405')
    root.title("Focus.")
    
    root.columnconfigure(0,weight=2)
    root.columnconfigure(1,weight=1)
    root.rowconfigure(0,weight=1)
    taskFrame = ttk.LabelFrame(root, text='Tasks ', padding=50)
    taskFrame.grid(row=0,column=0)
    taskFrame['border']=2
    taskFrame['relief']='ridge'
    
    sizegrip = ttk.Sizegrip(root)
    sizegrip.place(relx=1, rely=1, anchor=tk.SE)
    
    tk.Label(text="Timer be here").grid(row=0,column=1)
    for i in range(10):
        tk.Label(taskFrame, text="Task"+str(i)).grid(row=i,column=0)
    
    
    root.mainloop()
        
    

if __name__ == "__main__":
    main(data_dir)
