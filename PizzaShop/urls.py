"""PizzaShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pizza.views import get_all_pizza,add_pizza,delete_order,get_order_by_size,get_order_by_type,get_order, update_order

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/pizza',get_all_pizza),
    path('api/add/pizza',add_pizza),
    path('api/delete/pizza/<int:id>',delete_order),
    path('api/get/pizza/size',get_order_by_size),
    path('api/get/pizza/<int:id>',get_order),
    path('api/get/pizza/type',get_order_by_type),
    path('api/update/pizza/<int:id>',update_order),
]
