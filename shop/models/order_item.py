from django.db import models
from django.core.validators import MinValueValidator

class Order_Item(models.Model):
    order = models.ForeignKey(
        'Order',
        on_delete=models.CASCADE,
        null=False,
        related_name='order_items'
    )
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        null=False,
    )
    quantity = models.IntegerField(
        default=0, 
        null=False, 
        validators=[
            MinValueValidator(0)
        ]
    )