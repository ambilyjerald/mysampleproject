from django.shortcuts import render, redirect

from demo_app.forms import todo_form
from demo_app.models import todo


# Create your views here.
def dash(request):
    return render(request, 'dashboard.html')


def home(request):
    return render(request,'index.html')


def forms(request):
    data=todo_form()
    if request.method=='POST':
        obj=todo_form(request.POST)
        if obj.is_valid():
            obj.save()
            return redirect("/")
    return render(request,'modelform.html',{'formkey':data})



def data(request):
    data=todo.objects.all()
    return render(request,"child.html",{'formkey':data})

def delete_1(request,id):
    data = todo.objects.get(id=id)
    data.delete()
    return redirect('test3')

def update_1(request,id):
    n=todo.objects.get(id=id)
    form= todo_form(instance=n)
    if request.method=='POST':
        form=todo_form(request.POST,instance=n)
        if form.is_valid():
            form.save()
            return redirect('test3')
    return render(request,"update.html",{"form":form})

