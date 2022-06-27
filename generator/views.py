from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request,"home.html")

def password(request):

    char=list('abcdefghijklmnopqrstuvwxyz')

    length=int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        char.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        char.extend(list('!@#$%^&*()'))

    if request.GET.get('number'):
        char.extend(list('0123456789'))

    # if request.GET.get('number'):


    thepassword=''
    for x in range(length):
        thepassword+=random.choice(char)

    return render(request,"password.html",{'password':thepassword})