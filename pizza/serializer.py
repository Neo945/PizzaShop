from rest_framework import serializers
from .models import Pizza, Topping

class PizzaSerializer(serializers.ModelSerializer):
    topping = serializers.SerializerMethodField('get_toppings')
    def get_toppings(self,value):
        return ToppingSerializer(value.topping,many=True).data
    
    class Meta:
        model = Pizza
        fields = ['id','name','timestamp','size','topping','type','user']

class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = ['id','topping']

class PizzaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = ['name','type','size']