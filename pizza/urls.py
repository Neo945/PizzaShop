from django.urls import path
from .views import (
    get_all_pizza,
    add_pizza,
    delete_order,
    get_order_by_size,
    get_order_by_type,
    get_order, 
    update_order
)
app_name = 'pizza'
urlpatterns = [
    path('pizza',get_all_pizza),
    path('add/pizza',add_pizza),
    path('delete/pizza/<int:id>',delete_order),
    path('get/pizza/size',get_order_by_size),
    path('get/pizza/<int:id>',get_order),
    path('get/pizza/type',get_order_by_type),
    path('update/pizza/<int:id>',update_order),
]
