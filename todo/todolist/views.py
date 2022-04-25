from asyncio import Task
from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic.list import ListView
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from requests import delete
from .forms import RegisterUserForm,TaskForm,UpdateUserForm
from .models import Task
from django.contrib.auth.models import User
import datetime,calendar
from datetime import datetime,timedelta
from django.utils import timezone
# Create your views here.


@login_required(login_url='login')
def home(request):
    logout(request)
    return render(request,'login.html')

@login_required(login_url='login')
def finalweekdata(request,tasks):
    
    weekcount=[0,0,0,0,0,0,0] #Sun-Sat [ 1 - 7 ]
    todayweekday = datetime.today().weekday()
    totaltasks = 0
    if todayweekday == 6:#Sunday
        for i in range(1,2):
            totaltasks += Task.objects.filter(user=request.user).filter(createdon__week_day = i).count()
        weekcount[0] = Task.objects.filter(user=request.user,complete=True).filter(createdon__week_day = 1).count()
    if todayweekday == 0: #Monday
        for i in range(1,3):
            totaltasks += Task.objects.filter(user=request.user).filter(createdon__week_day = i).count()
        weekcount[0] = Task.objects.filter(user=request.user,complete=True).filter(createdon__week_day = 1).count()
        weekcount[1] = Task.objects.filter(user=request.user,complete=True).filter(createdon__week_day = 2).count()
        print(totaltasks,weekcount)
    if todayweekday == 1:#Tuesday
        for i in range(1,4):
            totaltasks += Task.objects.filter(user=request.user).filter(createdon__week_day = i).count()
        weekcount[0] = Task.objects.filter(user=request.user,complete=True).filter(createdon__week_day = 1).count()
        weekcount[1] = Task.objects.filter(user=request.user,complete=True).filter(createdon__week_day = 2).count()
        weekcount[2] = Task.objects.filter(user=request.user,complete=True).filter(createdon__week_day = 3).count()
    if todayweekday == 2:#Wednesday
        for i in range(1,5):
            totaltasks += Task.objects.filter(user=9).filter(createdon__week_day = i).count()
        weekcount[0] = Task.objects.filter(user=request.user,complete=True).filter(createdon__week_day = 1).count()
        weekcount[1] = Task.objects.filter(user=request.user,complete=True).filter(createdon__week_day = 2).count()
        weekcount[2] = Task.objects.filter(user=request.user,complete=True).filter(createdon__week_day = 3).count()
        weekcount[3] = Task.objects.filter(user=request.user,complete=True).filter(createdon__week_day = 4).count()
    if todayweekday == 3:#Thursday
        for i in range(1,6):
            totaltasks += Task.objects.filter(user=9).filter(createdon__week_day = i).count()
        weekcount[0] = Task.objects.filter(user=request.user,complete=True).filter(createdon__week_day = 1).count()
        weekcount[1] = Task.objects.filter(user=request.user,complete=True).filter(createdon__week_day = 2).count()
        weekcount[2] = Task.objects.filter(user=request.user,complete=True).filter(createdon__week_day = 3).count()
        weekcount[3] = Task.objects.filter(user=request.user,complete=True).filter(createdon__week_day = 4).count()
        weekcount[4] = Task.objects.filter(user=request.user,complete=True).filter(createdon__week_day = 5).count()
    if todayweekday == 4:#Friday
        for i in range(1,7):
            totaltasks += Task.objects.filter(user=9).filter(createdon__week_day = i).count()
        weekcount[0] = Task.objects.filter(user=request.user,complete=True).filter(createdon__week_day = 1).count()
        weekcount[1] = Task.objects.filter(user=request.user,complete=True).filter(createdon__week_day = 2).count()
        weekcount[2] = Task.objects.filter(user=request.user,complete=True).filter(createdon__week_day = 3).count()
        weekcount[3] = Task.objects.filter(user=request.user,complete=True).filter(createdon__week_day = 4).count()
        weekcount[4] = Task.objects.filter(user=request.user,complete=True).filter(createdon__week_day = 5).count()
        weekcount[5] = Task.objects.filter(user=request.user,complete=True).filter(createdon__week_day = 6).count()
    if todayweekday == 5:#Saturday
        for i in range(1,8):
            totaltasks += Task.objects.filter(user=request.user).filter(createdon__week_day = i).count()
        weekcount[0] = Task.objects.filter(user=request.user,complete=True).filter(createdon__week_day = 1).count()
        weekcount[1] = Task.objects.filter(user=request.user,complete=True).filter(createdon__week_day = 2).count()
        weekcount[2] = Task.objects.filter(user=request.user,complete=True).filter(createdon__week_day = 3).count()
        weekcount[3] = Task.objects.filter(user=request.user,complete=True).filter(createdon__week_day = 4).count()
        weekcount[4] = Task.objects.filter(user=request.user,complete=True).filter(createdon__week_day = 5).count()
        weekcount[5] = Task.objects.filter(user=request.user,complete=True).filter(createdon__week_day = 6).count()
        weekcount[6] = Task.objects.filter(user=request.user,complete=True).filter(createdon__week_day = 7).count()
    
    c=0
    p=0
    for task in tasks:
        if task.complete == True:
            c=c+1
        if task.complete == False:
            p=p+1
    t=c+p
    if c==0:
        per="0"
    else:
        per = (c/(c+p))*100
        per = str(per)

    wc = sum(weekcount)
    wp = totaltasks - wc
    if wc == 0:
        wper = "0"
    else:
        wper = (wc/(wc+wp))*100
        wper = str(wper)

    context={
        "tasks":tasks,
        "t":t,
        "c":c,
        "p":p,
        "per":per,
        "tt":totaltasks,
        "wc":wc,
        "wp":wp,
        "wper":wper,
        "twc":weekcount,
        }
    return context


def ulogin(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username,password = password)
        if user is not None:
            login(request,user)
            #return redirect('register')
            if (request.user.is_authenticated):
                tasks = Task.objects.filter(user = request.user)
                context = finalweekdata(request,tasks)
                return render(request,'todolist.html',context=context)
        else:
            messages.error(request,("There was an error! while logging in...."))
            return render(request,'login.html')
    logout(request)
    return render(request,'login.html')

def ulogout(request):
    logout(request)
    return render(request,'login.html')

def uregister(request):
    if request.method=="POST":
        print(request.POST)
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            #username = form.changed_data['username']
            #password = form.changed_data['password1']
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(username = username,password = password )
            login(request,user)
            if (request.user.is_authenticated):
                tasks = Task.objects.filter(user = request.user)
                context = finalweekdata(request,tasks)
                return render(request,'todolist.html',context=context)
        else:
            messages.error(request,("There was an error! while Register in...."))
            return render(request,'register.html')
    elif(request.user.is_authenticated):
            tasks = Task.objects.filter(user = request.user)
            context = finalweekdata(request,tasks)
            messages.error(request,("You are Already Registered...."))
            return render(request,'todolist.html',context=context)
    else:
        return render(request,'register.html')

@login_required(login_url='login')
def userdetails(request,id):
    if (request.user.is_authenticated):
        users = User.objects.filter(pk = id)
        context={
            "users":users
        }
        return render(request,'userdetails.html',context=context)

@login_required(login_url='login')
def updateuserdetails(request,id):
    if request.method=="POST":
        print(request.POST)
        form = UpdateUserForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            logout(request)
            messages.success(request,("Details Updated Please Login again...."))
            return render(request,'login.html')
        else:
            if (request.user.is_authenticated):
                users = User.objects.filter(pk = id)
                context={
                "users":users
                }
                messages.error(request,("There was an Error! while Editing Your Details...."))
                return render(request,'userdetails.html',context=context)

@login_required(login_url='login')
def todolist(request):
    if request.user.is_authenticated and request.method=="POST":
        cuser = request.user
        print(request.POST)
        form = TaskForm(request.POST)
        if form.is_valid():
            todoform = form.save(commit=False)
            todoform.user = cuser
            todoform.save()
            tasks = Task.objects.filter(user = request.user)
            context = finalweekdata(request,tasks)
            return render(request,'todolist.html',context=context)
        else:
            tasks = Task.objects.filter(user = request.user)
            context = finalweekdata(request,tasks)
            messages.error(request,("There was an Error! while Creating Your Task...."))
            return render(request,'todolist.html',context=context)
    elif(request.user.is_authenticated):
        tasks = Task.objects.filter(user = request.user)
        context = finalweekdata(request,tasks)
        return render(request,'todolist.html',context=context)
    else:
        messages.error(request,("Please Login or Register to Continue...."))
        return render(request,'login.html')

@login_required(login_url='login')
def updatetodolist(request,id):
    tasks = Task.objects.filter(pk = id,user = request.user)
    context={
    "tasks":tasks
    }
    return render(request,'updatetodolist.html',context=context)

@login_required(login_url='login')
def updatetask(request,id):
    if request.method=="POST":
        print(request.POST)
        form = TaskForm(request.POST)
        if form.is_valid():
            form = Task.objects.get(pk = id)
            form.title = request.POST['title']
            form.description = request.POST['description']
            if request.POST.get('complete', False) == 'on':
                form.complete = True
            else:
                form.complete = False
            #print(request.POST.get('complete', False))
            form.save()
            tasks = Task.objects.filter(user = request.user)
            context = finalweekdata(request,tasks)
            return render(request,'todolist.html',context=context)
        else:
            messages.error(request,("There was an Error! while Updating Your Task...."))
            return render(request,'todolist.html')
    else:
        tasks = Task.objects.filter(pk = id,user = request.user)
        context = finalweekdata(request,tasks)
        return render(request,'todolist.html',context=context)

@login_required(login_url='login')
def deletetodo(request,id):
    Task.objects.get(pk = id).delete()
    tasks = Task.objects.filter(user = request.user)
    context = finalweekdata(request,tasks)
    return render(request,'todolist.html',context=context)

