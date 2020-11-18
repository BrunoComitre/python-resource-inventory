from django.db import models

# Create your models here.


class Product(models.Model):  # Definição dos produtos, armazenado no banco de dados.
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return self.description
