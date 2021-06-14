from django.shortcuts import render
from .models import Task
from django.http import HttpResponse , HttpResponseRedirect
from django.urls import reverse

# Create your views here.



def index(request):
    task_list = Task.objects.order_by('date')
    row_colors = ["primary" , "secondary" , "success" ,"danger" ,"warning", "info" ,"light" , "dark"]
    return render(request , 'Todo/Todoindex.html' , {"task_list" : task_list , "row_colors":row_colors})

def create(request):
    if request.method == "POST":
        print(request.POST)
        task = request.POST['Newtask']
        date = request.POST['TaskTime'].replace("T"," ")
        status = False
        Newtask = Task(task=task , date=date , status=status)
        Newtask.save()
        # return HttpResponse("Hi Added")
        print("Created new Task :" + request.POST['Newtask'] + "time: " + request.POST['TaskTime'].replace("T"," "))
        return HttpResponseRedirect(reverse('Todo:index'))

def complete(request , id):
    comp_task = Task.objects.get(id=id)
    comp_task.status = True
    comp_task.save()
    print("Completed Task id :" + id)
    return HttpResponse("Completed Task id :" + id)

def delete(request , id):
    del_task = Task.objects.get(id=id)
    del_task.delete()
    print("Deleted Task id :" + id)
    return HttpResponse("Deleted Task id :" + id)
