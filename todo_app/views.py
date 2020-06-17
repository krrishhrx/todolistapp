from django.shortcuts import render, redirect
from django.http import HttpResponse
from todo_app.models import List
from todo_app.forms import ListForm
# Create your views here.

def index(request):
    items = List.objects.all()
    form = ListForm(request.POST)
    if form.is_valid():
        form.save()
        return render(request, 'index.html',{ 'items': items })
    return render(request, 'index.html',{ 'items': items })

def trash(request, id):
    items = List.objects.get(id = id)
    items.delete()
    return redirect('/')

def update(request , id):
    return HttpResponse("HI Updater")