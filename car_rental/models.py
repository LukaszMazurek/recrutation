from django.db import models

"""
This models will be mapped to sql tables.
"""


class Client(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    def __str__(self):
        return f"name: {self.name} surname {self.surname}"


class Car(models.Model):
    mark = models.CharField(max_length=100)
    production_date = models.DateField()

    # foreign key for many to one relationship
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f"mark: {self.mark} production_date: {str(self.production_date)}"
