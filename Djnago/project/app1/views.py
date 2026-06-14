from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    person={
        'name':'anson',
        'age':20,
        'place':'kottayam',
    }
    return render(request,'home.html',person)
def about(request):
    numbers={
        'num1':10,
    }
    return render(request,'about.html',numbers)
def booking(request):
    numbers={
        'num1':[1,2,3,4,5,6,7,8]
    }
    return render(request,'booking.html',numbers)
def doctors(request):
    return render(request,'doctors.html')
def contact(requset):
    return render(requset,'contact.html')


    