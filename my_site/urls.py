from django.contrib import admin
from django.urls import path, include, re_path
from shop import views #Поключение представления

product_lists = [ 
    path('', views.product),
    path('new-product', views.new_products),
    path('top-product', views.top_products),
]

urlpatterns = [ #Указание маршрутов
    path('admin/', admin.site.urls),
    path('', views.index),
    re_path(r'^about/contact', 
            views.contact, 
            kwargs={
                'name': 'Bob', 
                'age': 40, 'email': 
                'bob@gmail.com'
            }),
    re_path(r'^about', views.about),
    path('brw-info', views.browser_info),
    path('user/<str:name>', views.user),
    path('user/<str:name>/<int:age>', views.user),
    path('products/<int:id>/', include(product_lists)),
]
