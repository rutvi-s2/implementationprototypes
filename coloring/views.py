from django.shortcuts import render

def demo(request):
    return render(request, 'coloring/demo.html')

def new_interaction(request):
    return render(request, 'coloring/new_interaction.html')

def index(request):
    return render(request, 'coloring/index.html')