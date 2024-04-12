from tkinter.ttk import Combobox
import func
from acc import Account
from taskset import Task, TaskSet
from tkinter import *
from tkcalendar import Calendar
import datetime as dt
import pandas as pd

def display_ts():
    def button2_clicked(a):
        window3 = Tk()
        window3.config(background='black', padx=50, pady=50)
        window3.minsize(width=1500, height=300)
        lab2 = Label(window3, text=f"{a.title}\t{a.date.strftime('%d-%m-%Y')}", foreground='white', background='black')
        lab2.grid(column=0, row=0)
        en1 = Entry(window3, width=50)
        en1.insert(END, string='Brief description')
        en1.grid(column=1, row=1)
        # en2 = Entry(window3, width=30)
        # en2.insert(END, string='Task type')
        # en2.grid(column=2, row=1)
        lab23 = Label(window3, text='Choose task type: ', foreground='white', background='black')
        lab23.grid(column=2, row=1)
        cbbox = Combobox(window3, width=27)
        cbbox['values'] = ('Academics', 'Personal', 'Co-curricular', 'Extra-curricular')
        cbbox.grid(column=3, row=1)
        lab3 = Label(window3, text='Enter due date: ', foreground='white', background='black')
        lab3.grid(column=0, row=2)
        cal = Calendar(window3, selectmode='day', year=dt.datetime.now().year, month=dt.datetime.now().month, day=dt.datetime.now().day)
        cal.grid(column=1, row=2)
        lab4 = Label(window3, text='Enter weight: ', foreground='white', background='black')
        lab4.grid(column=4, row=1)
        var = IntVar()
        sc = Scale(window3, from_=1, to=10, variable=var, orient=HORIZONTAL, background='black', foreground="#1260CC")
        sc.grid(column=5, row=1)
        but3 = Button(window3, text='Add Task', background="#1260CC", foreground='white', command=lambda:func.button3_clicked(window3, a, en1, cbbox, cal, sc))
        but3.grid(column=2, row=2)
        df=pd.read_csv(f"{a.accname}.csv",header=None)
        j=0;
        for i in df.itertuples():
            def check(n):
                if n.get()==1:
                    i[6] = True
                    
            if(i[5]==a.title):
                print(i)
                n = IntVar()
                cb=Checkbutton(window3, text=f"{i[3]}\t{i[1]}\t{i[2]}\t{i[6]}",command=lambda:check(n),variable=n, bg='black', fg='white', activebackground='black', activeforeground='white',selectcolor="black")
                cb.grid(row=3+j, column=0)
                j=j+1
        window3.mainloop()
    i = 1
    col = 0
    for ts in acc1.setlist:
        # Command (function to display the taskset)
        but = Button(text=ts.title, background="#FF83C1", foreground='white', width=50, height=5, command=lambda:button2_clicked(ts))
        but.grid(column=col, row=i)
        col += 1
        if col == 2:
            i += 1
            col = 0

def create_ts():
    def button1_clicked():
        title = entry.get()
        ts1 = TaskSet(title, acc1.name)
        acc1.addtaskset(ts1)
        display_ts()
        window2.destroy()

    window2 = Tk()
    window2.config(background='black', pady=50, padx=50)
    entry = Entry(window2, width=50)
    entry.insert(END, string='TaskSet-untitled')
    entry.grid(column=0, row=0)
    but2 = Button(window2, text='Create', background='#1260CC', foreground='white', command=button1_clicked)
    but2.grid(column=0, row=1)
    window2.mainloop()


window = Tk()
window.config(background='black', pady=50, padx=50)
window.minsize(width=1000, height=300)
window.geometry("900x500")

acc1 = Account('User0', '20', 'f')

but1 = Button(text='Create TaskSet', background='#1260CC', foreground='white', command=create_ts)
but1.grid(column=0, row=0, columnspan=2)

display_ts()

window.mainloop()