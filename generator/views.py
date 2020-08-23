from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    return render(request, 'generator/home.html', {'homePageColor': 'Green'})


def plants(request):
    return HttpResponse("<h1 style='color: blue'>Life can only survive on <i style='color: black'>Earth</i> with plants implementation!</h1>")


def password(request):
    numbers = int(request.GET.get('length'))
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if(request.GET.get('numbers')):
        characters.extend('0123456789')
    if (request.GET.get('upperCase')):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if(request.GET.get('specialChar')):
        characters.extend('!@#$%^&*()~')
    password = ''
    for num in range(numbers):
        password += random.choice(characters)
    return render(request, 'generator/password.html', {'password': password})


def aboutApp(request):
    return render(request, 'generator/aboutApp.html')
