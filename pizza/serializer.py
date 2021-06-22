from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework.decorators import action
from .models import Pizza, Topping
from django.conf import settings

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

class UpdateActionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    type = serializers.CharField(required=False)
    size = serializers.CharField(required=False)
    toppings = serializers.ListField(required=False)

    def validate_action(self,value):
        if value not in ['add','remove']:
            raise serializers.ValidationError('This action is not valid')
        return value
    def validate_type(self,value):
        print(value)
        if value not in settings.PIZZA_TYPE:
            raise serializers.ValidationError('This type is not valid')
        return value
    def validate_size(self,value):
        if value not in settings.PIZZA_SIZE:
            raise serializers.ValidationError('This size is not valid')
        return value
    def validate_toppings(self,value):
        if type(value)!=list:
            raise serializers.ValidationError('This datatype is not valid')
        return value
