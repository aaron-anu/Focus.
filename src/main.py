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

def addWindow(parent,taskFrame,dataframe,tasksFilePath):
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
    
    def saveTask(dataframe,tasksFilePath,root):
        title=titleEntry.get()
        desc=descEntry.get()
        dueTime_Unparsed=dueEntry.get()
        birthTime=datetime.now().strftime("%B %d, %Y - %I:%M %p") 
        if dueTime_Unparsed:
            dueTime=dateparser.parse(dueTime_Unparsed).strftime("%B %d, %Y - %I:%M %p") 
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
        dataframe.to_csv(tasksFilePath, index=False)
        refresh_task_list(root, taskFrame, dataframe, tasksFilePath)
        add.destroy()

        
    tk.Button(add, text="Save", command=lambda: saveTask(dataframe,tasksFilePath,parent)).pack()
    
def create_task_card(root, parent,row_data, dataframe, tasksFilePath,i):
    # A container for one single task row
    card = tk.Frame(parent, highlightbackground="#ddd", 
                    highlightthickness=1, padx=10, pady=10)
    card.pack(fill="x", pady=5, padx=10)

    # Status Indicator (Done/Not Done)
    color = "green" if row_data['done'] else "red"
    tk.Label(card, text="●", fg=color ).pack(side="left")
    
    # Task Title
    tk.Label(card, text=row_data['title'], 
             font=("Arial", 12, "bold")).pack(side="left")
    
    #button near tasks
    tk.Button(card, text='Finish',command=lambda: complete_task(root, parent,dataframe,tasksFilePath,row_data['title'],i)).pack(side="right")
    # Due Date
    tk.Label(card, text=f"Due: {row_data['duetime']}", 
             font=("Arial", 10, "italic")).pack(side="right", padx=10)
    
    
def refresh_task_list(root, taskFrame, tasksDataframe, tasksFilePath):
    for widget in taskFrame.winfo_children():
        widget.destroy()

    for i in range(tasksDataframe.shape[0]):
        create_task_card(root, taskFrame,tasksDataframe.iloc[i].to_dict(), tasksDataframe, tasksFilePath,i)
    
    tk.Button(taskFrame, text="Add New Task", 
               command=lambda: addWindow(root, taskFrame, tasksDataframe, tasksFilePath)).pack()

def complete_task(root,taskFrame ,dataframe,tasksFilePath,title,i):
    dataframe.at[i, 'done'] = not dataframe.at[i, 'done']
    dataframe.to_csv(tasksFilePath, index=False)
    refresh_task_list(root, taskFrame, dataframe, tasksFilePath)
        
        
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
    
    for i in range(tasksDataframe.shape[0]):
        create_task_card(root, taskFrame,tasksDataframe.iloc[i].to_dict(), tasksDataframe, tasksFilePath,i)
        
        
    timerFrame = ttk.LabelFrame(root, text='Tasks ', padding=50)
    timerFrame.grid(row=0,column=1)
    
    #Themed Tkinter
    sizegrip = ttk.Sizegrip(root)
    sizegrip.place(relx=1, rely=1, anchor=tk.SE)
    
    tk.Label(timerFrame,text="Timer be here").grid(row=0,column=1)

    tk.Button(taskFrame, text='Add New Task',command=lambda: addWindow(root,taskFrame,tasksDataframe,tasksFilePath)).pack()
    
    root.mainloop()
        
    

if __name__ == "__main__":
    main(data_dir)
