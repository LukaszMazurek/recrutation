from django.contrib import admin
from car_rental.models import Car, Client

"""
Register models to django admin
"""
admin.site.register(Car)
admin.site.register(Client)
