from django.shortcuts import render
from django import forms

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority= forms.IntegerField(label="Priority", min_value=1, max_value=10)

tasks = ["baz", "ball", "cricket","football"]
# Create your views here.

def index(request):
    return render(request, "tasks/index.html",{
        "Tasks": tasks
    })

def add(request):
    return render(request, "tasks/add.html",{
        "form": NewTaskForm()
    })