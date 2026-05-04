import os
import dateparser
from datetime import datetime
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as m
import pandas as pd

from lib import tasks

# Specify custom data directory. By default ../data/
data_dir=None

def addWindow(parent,taskFrame,dataframe):
    add = tk.Toplevel(parent)
    add.title("Add Window")
    add.geometry("300x200")

    tk.Label(add, text="Enter title of task: ").pack()
    titleEntry=tk.Entry(add)
    titleEntry.pack()
    tk.Label(add, text="Enter description: ").pack()
    descEntry=tk.Entry(add)
    descEntry.pack()
    tk.Label(add, text="Enter due time: ").pack()
    dueEntry=tk.Entry(add)
    dueEntry.pack()
    
    def saveTask(dataframe):
        title=titleEntry.get()
        desc=descEntry.get()
        dueTime_Unparsed=dueEntry.get()
        birthTime=datetime.now()
        if dueTime_Unparsed:
            dueTime=dateparser.parse(dueTime_Unparsed)
        else:
            dueTime=None
        
        new_row = pd.DataFrame([{
            "title": title,
            "birthtime": birthTime,
            "duetime": dueTime,
            "done": False,
            "desc": desc
        }])
        dataframe = pd.concat([dataframe, new_row], ignore_index=True)
        
    tk.Button(add, text="Save", command=lambda: saveTask(dataframe)).pack()

def main(data_dir):

    # create data dir
    if data_dir is None:
        data_dir = os.path.dirname(os.path.abspath(__file__)) + "/../data"
    if not os.path.exists(data_dir):
        os.mkdir(data_dir)
    tasksFilePath=data_dir+'/tasks.csv'
    
    if os.path.exists(tasksFilePath):
        tasksDataframe=pd.read_csv(tasksFilePath)
    else:
        tasksDataframe = pd.DataFrame(columns=["title", "birthtime", "duetime", "done", "desc"])
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
    
        
    timerFrame = ttk.LabelFrame(root, text='Tasks ', padding=50)
    timerFrame.grid(row=0,column=1)
    
    #Themed Tkinter
    sizegrip = ttk.Sizegrip(root)
    sizegrip.place(relx=1, rely=1, anchor=tk.SE)
    
    tk.Label(timerFrame,text="Timer be here").grid(row=0,column=1)

    tk.Button(taskFrame, text='Add New Task',command=lambda: addWindow(root,taskFrame,tasksDataframe)).pack()
    
    
    root.mainloop()
        
    

if __name__ == "__main__":
    main(data_dir)
