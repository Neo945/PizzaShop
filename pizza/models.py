from django.core.exceptions import ValidationError
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL
def is_valid(value):
    if value.lower() not in ['regular','square']:
        raise ValidationError('Not a valid type')

def is_size_valid(value):
    if value.lower() not in ['small','large','medium','extra large']:
        raise ValidationError('Not a valid size')

class Topping(models.Model):
    topping = models.CharField(max_length=50,null=False)

class Pizza(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    name = models.CharField(max_length=50,null=False,blank=False)
    type = models.CharField(validators=[is_valid],max_length=7,null=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    size = models.CharField(max_length=50,null=False,validators=[is_size_valid])
    topping = models.ManyToManyField('topping',related_name='toppings',blank=True,through='Topping_pizza')
    
    def __str__(self) -> str:
        return self.name

class Topping_pizza(models.Model):
    pizza = models.ForeignKey(Pizza,on_delete=models.CASCADE)
    topping = models.ForeignKey(Topping,on_delete=models.CASCADE)
