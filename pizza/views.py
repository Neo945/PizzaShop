from pizza.models import Pizza, Topping
from pizza.serializer import PizzaCreateSerializer, PizzaSerializer
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import timezone
import datetime

# Create your views here.
@api_view(['GET'])
def get_pizza(request):
    return Response(PizzaSerializer(Pizza.objects.all(),many=True).data,status=200)

@api_view(['GET','POST'])
def add_pizza(request):
    if request.method == 'POST':
        data = request.data
        serial = PizzaCreateSerializer(data=data)
        if serial.is_valid():
            p = serial.save(user = request.user)
            for topping in data['topping']:
                qs = Topping.objects.get_or_create(topping=topping)
                p.topping.add(qs[0].id)
            return Response({'message':'Ordered Successfully','order_no':p.id},status=201)
        return Response({'message':'form is not valid'},status=401)
    return Response({},status=200)

@api_view(['GET','POST'])
def delete_order(request):
    if request.method == 'POST':
        qs = Pizza.objects.filter(pk=request.data.get('id')).first()
        if (qs.timestamp + datetime.timedelta(minutes=20)) < timezone.now():
            return Response({'message':'order cannot be deleted'},status=201)
        Pizza.objects.delete(pk=request.data.get('id'))
        return Response({'message':'order deleted successfully'},status=201)
    return Response({},status=200)

@api_view(['GET'])
def get_order(request):
    qs = Pizza.objects.filter(pk=request.data.get('id'))
    if qs.exists():
        return Response(PizzaSerializer(qs.first()).data,status=200)
    return Response({'message':'order not found'},status=404)
