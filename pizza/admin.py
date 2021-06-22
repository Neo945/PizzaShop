from django.contrib import admin
from .models import Pizza,Size,Topping,Size_pizza,Topping_pizza

# Register your models here.
admin.site.register(Pizza)
admin.site.register(Size_pizza)
admin.site.register(Size)
admin.site.register(Topping)
admin.site.register(Topping_pizza)