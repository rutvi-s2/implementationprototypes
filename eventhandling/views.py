from django.shortcuts import render
from django.http import HttpResponse


def a(request):
    return render(request, 'eventhandling/a.html')

def b(request):
    return render(request, 'eventhandling/b.html')

def index(request):
    return render(request, 'eventhandling/index.html')
