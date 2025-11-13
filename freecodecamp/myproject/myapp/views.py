from django.http import HttpResponse
from django.shortcuts import render
from .models import Userdata
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,"./About.html")
def insert(request):
    return render(request,"./insert.html")

def insert_user_data(request):
    firstname=request.POST['fname']
    lastname=request.POST['lname']
    phoneno=request.POST['phno']
    aadhar=request.POST['aadhar']
    Age=request.POST['age']

    obj=Userdata()
    obj.Firstname=firstname
    obj.Lastname=lastname
    obj.PhoneNumber=phoneno
    obj.AadharNumber=aadhar
    obj.Age=Age
    obj.save()
    return render(request,"./about.html")

def read_data(request):
    return render(request,"./read.html")

def show_data(request):
    data=Userdata.objects.all()
    return render(request,"table.html",context={'data':data})

def filter_data(request):
    print(Userdata.objects.filter(Firstname__contains="va"))
    return HttpResponse("Records Filtered....")
