from django.contrib import admin
from .models import PizzaToppings, PizzaStore, PizzaSize

# Register your models here.

admin.site.register(PizzaToppings)
admin.site.register(PizzaSize)
admin.site.register(PizzaStore)