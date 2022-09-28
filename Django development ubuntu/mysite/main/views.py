from sys import implementation
from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList,Item


# Create your views here.

def index(response,id):
    ls = ToDoList.objects.get(id=id)
    return render(response,"main/list.html",{"ls":ls})

def index_name(response,name):
    ls = ToDoList.objects.get(name=name)
    item = ls.item_set.get(id=1)
    return HttpResponse("<h1>%s </h!><br></br><p>%s</p>"% (ls.name,str(item.text)))

def home(response):

    return render(response,"main/home.html",{})