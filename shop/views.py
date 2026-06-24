from django.shortcuts import render
from django.http import HttpResponse #Для работы с запросами

def index(request):
    header = 'hello, user'
    array = [1, 2, 3, 4, 5]
    user = {'name': 'Bob', 'age': 23}
    address = ('Ленина', 2, 54, 23)

    data = {
        'header': header,
        'array': array,
        'user': user,
        'address': address
    }

    return render(request, "shop/index.html", context=data)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return render(request, 'shop/contact.html')