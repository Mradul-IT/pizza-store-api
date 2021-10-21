from django.urls import path
from pizza import views
from pizza.views import (PizzaSizeViewSet, PizzaToppingsViewSet, PizzaStoreViewSet)

from rest_framework import routers

router = routers.DefaultRouter()
router.register('pizzasize',PizzaSizeViewSet)
router.register('pizzatoppings',PizzaToppingsViewSet)
router.register('pizzastore',PizzaStoreViewSet)

urlpatterns = [
    
] + router.urls