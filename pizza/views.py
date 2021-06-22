from pizza.models import Pizza
from pizza.serializer import PizzaSerializer
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def get_pizza(request):
    return Response(PizzaSerializer(Pizza.objects.all(),many=True).data,status=200)