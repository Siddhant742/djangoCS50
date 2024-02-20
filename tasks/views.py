from django.shortcuts import render

tasks = ["baz", "ball", "cricket","football"]
# Create your views here.

def index(request):
    return render(request, "tasks/index.html",{
        "Tasks": tasks
    })