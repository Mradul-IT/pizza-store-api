from rest_framework import serializers
from pizza.models import PizzaSize,PizzaToppings,PizzaStore


class PizzaSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaSize
        fields = ['size', 'id']


class PizzaToppingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaToppings
        fields = ['topping', 'id']
     

class PizzaStoreSerializer(serializers.ModelSerializer):
    pizza_toppings = serializers.SlugRelatedField(slug_field='topping',queryset=PizzaToppings.objects.all(),many=True)
    pizza_size = serializers.SlugRelatedField(slug_field='size',queryset=PizzaSize.objects.all(),many=False)
    
    class Meta:
        model = PizzaStore
        fields = ['id','pizza_type','pizza_size','pizza_toppings']

    