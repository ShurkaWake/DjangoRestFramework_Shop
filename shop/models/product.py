from django.db import models
from .category import Category

class Product(models.Model):
    name = models.CharField(max_length=255, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        null=False,
    )

    def __str__(self):
        return self.name