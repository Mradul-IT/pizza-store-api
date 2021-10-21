from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.validators import ValidationError
from rest_framework import status
from pizza.models import PizzaToppings,PizzaSize,PizzaStore
from pizza.serializers import PizzaSizeSerializer,PizzaToppingsSerializer,PizzaStoreSerializer
from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Create your views here.

class PizzaSizeViewSet(viewsets.ModelViewSet):
    """
    List of all sizes, or create a new size.
    """

    serializer_class = PizzaSizeSerializer
    queryset = PizzaSize.objects.all()


class PizzaToppingsViewSet(viewsets.ModelViewSet):
    """
    List of all toppings, or create a new topping.
    """
    serializer_class = PizzaToppingsSerializer
    queryset = PizzaToppings.objects.all()

class PizzaStoreViewSet(viewsets.ModelViewSet):
    """
    List of all pizza details.
    """
    serializer_class = PizzaStoreSerializer
    queryset = PizzaStore.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['pizza_type', 'pizza_size']


