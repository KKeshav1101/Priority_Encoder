from django.shortcuts import render,redirect,get_object_or_404
from Tasks.models import Task,Account
from Tasks.forms import AccountForm,TaskForm
import datetime as dt
import pickle
import os
from django.conf import settings
from Tasks.modeltesting import prep

# Load the model
file=open('Tasks\\pe.pkl','rb')
model = pickle.load(file)

def predict_task_weight(raw):
    # Assuming input_features is a list or array
    prediction = model.predict([prep(raw)])
    return prediction[0]


def extract(account):
    tasklist=account.tasklist
    if not tasklist:
        return None
    tasklist=eval(tasklist)
    tasks=[]
    for i in tasklist:
        task=Task.objects.get(id=i)
        tasks.append(task)
    tasks.sort(key=lambda x: x.task_weight,reverse=True)
    return tasks

# Login, Register in home, and actual list in homepage
def login(request):
    form=AccountForm()
    if(request.method=='POST'):
        form=AccountForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            qs=Account.objects.filter(username=username).first()
            if not qs:
                return render(request,'ack.html',{'msg':"Account Doesn't Exist"})
            request.session['username']=qs.id
            return render(request,'homepage.html',{'qs':qs,'form':TaskForm(),'tasks':extract(qs)})
    return render(request,'login.html',{'form':form})

def register(request):
    form=AccountForm()
    if request.method=='POST':
        form=AccountForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            qs=Account.objects.filter(username=username).first()
            if qs:
                return render(request,'ack.html',{'msg':"Account already Exists"})
            a=Account(username=username)
            a.save()
            request.session['username']=a.id
            return render(request,'homepage.html',{'qs':a,'form':TaskForm()})
    return render(request,'login.html',{'form':form})

def home(request):
    return render(request,'home.html')

def homepage(request):
    qs=Account.objects.get(id=request.session.get('username'))
    form=TaskForm()
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            desc=form.cleaned_data['Description']
            type=form.cleaned_data['Type']
            due=form.cleaned_data['Due_Date']
            #wt=form.cleaned_data['Weight']
            current_date=dt.date.today()
            raw=[desc,type,(due-current_date).total_seconds()/3600]
            wt=predict_task_weight(raw)
            t=Task(task_desc=desc,task_type=type,task_due=due,task_date=current_date,task_weight=wt,accname=qs.username)
            t.save()
            if not qs.tasklist:
                l=[]
            else:
                l=eval(qs.tasklist)
            l.append(t.id)
            qs.tasklist=str(l)
            qs.save()
            return render(request,'homepage.html',{'qs':qs,'form':form,'tasks':extract(qs)})
    return render(request,'homepage.html',{'qs':qs,'form':form})

def delete_task(request, task_id):
    if 'username' not in request.session:
        return redirect('login')  # Replace 'login' with your login view name

    qs = Account.objects.get(id=request.session['username'])
    form = TaskForm()

    # Ensure the task exists; if not, return a 404 error
    task = get_object_or_404(Task, id=task_id)

    # Remove the task ID from the tasklist
    if qs.tasklist:
        task_ids = eval(qs.tasklist)  # Convert tasklist from string to list
        if task_id in task_ids:
            task_ids.remove(task_id)
            qs.tasklist = str(task_ids)  # Convert back to string
            qs.save()

    # Delete the task from the database
    task.delete()

    # Redirect back to the homepage with updated data
    return render(request, 'homepage.html', {'qs': qs, 'form': form, 'tasks': extract(qs)})

def mark_completed(request, task_id):
    if 'username' not in request.session:
        return redirect('login')  # Replace 'login' with your login view name

    qs = Account.objects.get(id=request.session['username'])
    form = TaskForm()
    task=get_object_or_404(Task, id=task_id)
    task.completed=True
    task.save()
    return render(request, 'homepage.html', {'qs': qs, 'form': form, 'tasks': extract(qs)})
