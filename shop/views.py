from django.shortcuts import render
from django.http import HttpResponse #Для работы с запросами

class Person:

    def __init__(self, name):
        self.name = name

def index(request):
    
    data = {
        'data1': {
            'client_one': 'Иван Иванов',
            'client_two': 'Мария не звонить',
            'client_tree': 'Евгений рыбалка',
        },
        'users': ["Bob", "Petr", "Alex"],
    }

    return render(request, "shop/index.html", context=data)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return render(request, 'shop/contact.html')

