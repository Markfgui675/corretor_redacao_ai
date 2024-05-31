from django.shortcuts import render

def index(request):
    return render(request, 'corretor_ia/index.html')

def corretor(request):
    return render(request, 'corretor_ia/corretor.html')
