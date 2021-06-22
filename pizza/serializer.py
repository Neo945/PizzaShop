from rest_framework import serializers
from .models import Pizza, Size, Topping

class PizzaSerializer(serializers.ModelSerializer):
    
    size = serializers.SerializerMethodField('get_size')
    def get_size(self,value):
        return SizeSerializer(value.size,many=True).data
    
    topping = serializers.SerializerMethodField('get_toppings')
    def get_toppings(self,value):
        return ToppingSerializer(value.topping,many=True).data
    
    class Meta:
        model = Pizza
        fields = ['id','name','timestamp','size','topping']

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['id','size']

class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = ['id','topping']