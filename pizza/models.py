from django.core.exceptions import ValidationError
from django.db import models

def is_valid(value):
    if value.lower() not in ['regular','square']:
        raise ValidationError('Not a valid type')

def is_size_valid(value):
    if value.lower() not in ['small','large','medium','extra large']:
        raise ValidationError('Not a valid size')

class Size(models.Model):
    size = models.CharField([is_size_valid],max_length=50,null=False)

class Topping(models.Model):
    topping = models.CharField(max_length=50,null=False)

class Pizza(models.Model):
    name = models.CharField(max_length=50,null=False,blank=False)
    type = models.CharField([is_valid],max_length=7,null=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    size = models.ManyToManyField('size',related_name='sizes',blank=True,through='Size_pizza')
    topping = models.ManyToManyField('topping',related_name='toppings',blank=True,through='Topping_pizza')
    
    def __str__(self) -> str:
        return self.name

class Size_pizza(models.Model):
    pizza = models.ForeignKey(Pizza,on_delete=models.CASCADE)
    size = models.ForeignKey(Size,on_delete=models.CASCADE)

class Topping_pizza(models.Model):
    pizza = models.ForeignKey(Pizza,on_delete=models.CASCADE)
    topping = models.ForeignKey(Topping,on_delete=models.CASCADE)
