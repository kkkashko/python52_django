from django.contrib import admin
from django.urls import path, include, re_path
from shop import views #Поключение представления

urlpatterns = [ #Указание маршрутов
    path('admin/', admin.site.urls),
    path('', views.index),
    path('about/', views.about),
    path('contact/', views.contact),
]
