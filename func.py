from tkinter import *
from taskset import Task, TaskSet
import datetime as dt
import csv
import pandas as pd

def button3_clicked(window3, a, en1, cbbox, cal, sc):
    desc = en1.get()
    type = cbbox.get()
    due = cal.get_date()
    wt = sc.get()
    a.add_task(Task(desc, type, due, wt, a.title))
    en1.delete(0, END)
    cbbox.set('')
    cal.selection_set(dt.datetime.now())
    sc.set(1)
    f = open(f"{a.accname}.csv",'a')
    wr = csv.writer(f)
    wr.writerow([desc, type, due, wt, a.title,False])
    f.close()
    df=pd.read_csv(f"{a.accname}.csv",header=None)
    j=0;
    for i in df.itertuples():
        def check(n):
            if n.get()==1:
                i[6] = True
                df.to_csv(f"{a.accname}.csv")
        if(i[5]==a.title):
            print(i)
            n = IntVar()
            cb = Checkbutton(window3, text=f"{i[3]}\t{i[1]}\t{i[2]}\t{i[6]}",command=lambda:check(n), variable = n, bg='black', fg='white', activebackground='black', activeforeground='white',selectcolor="black")
            cb.grid(row=3+j, column=0)
            j=j+1