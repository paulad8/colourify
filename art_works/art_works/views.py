from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    return render(request, 'homepage.html')

def artists(request):
    return render(request, 'artists.html')

def movement(request):
    return render(request, 'movement.html')


