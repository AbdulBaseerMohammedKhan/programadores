import tkinter as tk
from tkinter import filedialog, Text
import os
root = tk.Tk()
root.title("SEPSIS DETECTION")
root.geometry("500x500")
root.configure(bg='SkyBlue1')
root.resizable(0,0)
def sym():
    a=tk.Tk()
    a.title("SYMPTOMS")
    a.geometry("300x300")
    a.configure(bg='rosybrown')
    w=tk.Label(a,text="THE SYMPTOMS OF SEPSIS ARE .........",bg='rosybrown')
    w.place(anchor='nw')
    a.mainloop()

def add():
    filename = filedialog.askopenfilename(initialdir="/",title="Select .csv files",filetypes=(("CSV FILES","*.csv"),("all files","*.*")))
    os.startfile(filename)
    
    
b=tk.Button(root,text="Predict",height=5,width=15,bg='red',fg='black',command=add)
b.place(relx=0.2,rely=0.5,anchor='c')
a=tk.Button(root,text="Symptoms",height=5,width=15,bg='yellow',fg='black',command=sym)
a.place(relx=0.5,rely=0.5,anchor='c')
c=tk.Button(root,text="Guidelines",height=5,width=15,bg='forestgreen',fg='black')
c.place(relx=0.8,rely=0.5,anchor='c')
tk.mainloop()

