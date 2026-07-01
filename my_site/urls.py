from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from shop import views #Поключение представления

urlpatterns = [ #Указание маршрутов
    path('admin/', admin.site.urls),
    path('', views.index),
    path('about/', TemplateView.as_view(template_name="shop/about.html", 
        extra_context={"header": "Подробная информация"})),
    path('contact/', TemplateView.as_view(template_name="shop/contact.html")),
]