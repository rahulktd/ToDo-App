from django.shortcuts import render, redirect

from ToDoApp.forms import ToDoForm
from ToDoApp.models import ToDo


# Create your views here.
def NewOne(request):
    return render(request, 'home.html')


def dash(request):
    return render(request, 'dBNew.html')


def NotFound(request):
    return render(request, '404.html')


def blank(request):
    return render(request, 'blank.html')


def button(request):
    return render(request, 'button.html')


def chart(request):
    return render(request, 'chart.html')


def element(request):
    return render(request, 'element.html')


def form(request):
    return render(request, 'form.html')


def signin(request):
    return render(request, 'signin.html')


def signup(request):
    return render(request, 'signup.html')


def table(request):
    return render(request, 'table.html')


def typography(request):
    return render(request, 'typography.html')


def widget(request):
    return render(request, 'widget.html')


# create ToDoApp
def addData(request):
    form = ToDoForm()
    if request.method == "POST":
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dash')
    return render(request, 'demo.html', {"form": form})


def dbn(request):
    return render(request, 'dBNew.html')


# read/view
def view(request):
    data = ToDo.objects.all()
    return render(request, 'addeddata.html', {"data": data})


# delete function
def delete(request, id):
    data = ToDo.objects.get(id=id)
    data.delete()
    return redirect("view")


# update function
def update(request, id):
    todo = ToDo.objects.get(id=id)
    form = ToDoForm(instance=todo)
    if request.method == 'POST':
        form = ToDoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect('view')
    return render(request,'new1.html', {'form': form})
