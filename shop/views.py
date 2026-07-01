from django.shortcuts import render
from django.http import HttpResponse #Для работы с запросами

class Person:

    def __init__(self, name):
        self.name = name

def index(request):
    
    return render(request, "shop/index.html", context={'tutorial': 12345})

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return render(request, 'shop/contact.html')

