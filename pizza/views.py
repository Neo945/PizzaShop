from django.conf import settings
from django.core.exceptions import ValidationError
from pizza.models import Pizza, Topping
from pizza.serializer import PizzaCreateSerializer, PizzaSerializer, UpdateActionSerializer
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.utils import timezone
import datetime
from rest_framework.permissions import IsAuthenticated

"""
Validated
"""
@permission_classes([IsAuthenticated])
@api_view(['GET','POST'])
def get_order_by_size(request):
    size = str(request.data.get('size'))
    qs = Pizza.objects.filter(size=size.lower())
    if size.lower() in settings.PIZZA_SIZE:
        return Response(PizzaSerializer(qs,many=True).data,status=200)
    return Response({'message':'Not a valid size or request'},status=400)

@permission_classes([IsAuthenticated])
@api_view(['GET','POST'])
def get_order_by_type(request):
    type = str(request.data.get('type'))
    qs = Pizza.objects.filter(type=type.lower())
    if type.lower() in settings.PIZZA_TYPE:
        return Response(PizzaSerializer(qs,many=True).data,status=200)
    return Response({'message':'Not a valid type or request'},status=400)

@permission_classes([IsAuthenticated])
@api_view(['GET'])
def get_order(request,id):
    qs = Pizza.objects.filter(pk=id)
    if qs.exists():
        return Response(PizzaSerializer(qs.first()).data,status=200)
    return Response({'message':'order not found'},status=404)

@permission_classes([IsAuthenticated])
@api_view(['GET'])
def get_all_pizza(request):
    return Response(PizzaSerializer(Pizza.objects.all(),many=True).data,status=200)

@permission_classes([IsAuthenticated])
@api_view(['GET','DELETE'])
def delete_order(request,id):
    qs = Pizza.objects.filter(pk=id)
    if qs.exists():
        qs = qs.first()
        if request.user == qs.user:
            if (qs.timestamp + datetime.timedelta(minutes=20)) < timezone.now():
                return Response({'message':'order cannot be deleted'},status=400)
            Pizza.objects.filter(pk=id).delete()
            return Response({'message':'order deleted successfully'},status=201)
        return Response({'message':'Not Authorized'},status=401)
    return Response({'message':'user not found'},status=200)

@permission_classes([IsAuthenticated])
@api_view(['GET','POST'])
def add_pizza(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            data = request.data
            serial = PizzaCreateSerializer(data=data)
            if serial.is_valid() and data.get('topping'):
                p = serial.save(user = request.user)
                for topping in data['topping']:
                    qs = Topping.objects.get_or_create(topping=topping.lower())
                    p.topping.add(qs[0].id)
                return Response({'message':'Ordered Successfully','order_no':p.id},status=201)
            return Response({'message':'form is not valid'},status=400)
        return Response({'message':'Not Authenticaed'},status=403)
    return Response({},status=200)
"""
{
"name":"pizza",
"size":"small",
"type":"regular",
"topping":["cheese","onion"]
}
"""

def is_valid(value):
    if value.lower() not in settings.PIZZA_TYPE:
        raise ValidationError('Not a valid type')

@permission_classes([IsAuthenticated])
@api_view(['GET','POST'])
def update_order(request,id):
    if request.method == 'POST':
        data = UpdateActionSerializer(data=request.data)
        if data.is_valid(raise_exception=True):
            data = data.data
            print(data)
            qs = Pizza.objects.filter(pk=data['id']).first()
            if request.user == qs.user:
                if (qs.timestamp + datetime.timedelta(minutes=20)) < timezone.now():
                    return Response({'message':'order cannot be Updated'},status=400)
                if data.get('action')=='add':
                    for topping in data.get('toppings'):
                        top = Topping.objects.get_or_create(topping=topping)
                        qs.topping.add(top[0])
                elif data.get('action')=='remove':
                    for topping in data.get('toppings'):
                        top = Topping.objects.get(topping=topping)
                        qs.topping.remove(top[0])
                if data.get('type'):
                    qs.type = data.get('type')
                    qs.save()
                if data.get('size'):
                    qs.size = data.get('size')
                    qs.save()
                if data.get('name'):
                    qs.name = data.get('name')
                    qs.save()
                return Response({'message':'order updated successfully'},status=201)
            return Response({'message':'Not Authorized'},status=403)
        return Response({'message':'Form not valid'},status=400)
    return Response({},status=200)