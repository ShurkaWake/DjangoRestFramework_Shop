from django.db import models
from django.utils.timezone import now

class Order(models.Model):
    user = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        null=False,
    )
    order_date = models.DateField(default=now, null=False)

    def get_order_items(self):
        from .order_item import Order_Item
        
        return Order_Item.objects.filter(order__pk=self.pk)

