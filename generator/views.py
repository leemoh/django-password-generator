from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,'generator/home.html')
def password(request):
    thepassword = ''
    characters=list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('Uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('SpecialCharacters'):
        characters.extend(list('!@#$%^&*~?'))
    if request.GET.get('Numbers'):
        characters.extend(list('0987654321'))
    length=int(request.GET.get('length'))
    if length >12:
        length=12
    elif length <5:
        length=5
    
    for x in range(length):
        thepassword+=random.choice(characters)

    return render(request,'generator/password.html', {'password':thepassword})
def about(request):
    return render(request,'generator/about.html')