from django.db import models
from django.contrib.auth import get_user_model

from product.models import Product

User = get_user_model()

class Order(models.Model):
    author = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, through='OrderItem')
    total_sum = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    STATUSES = [
        ('D', 'Delivered'),
        ('ND', 'Not Delivered')
    ]
    status = models.CharField(max_length=2, choices=STATUSES)
    PAYMENTS = [
        ('Card', 'Card'),
        ('Cash', 'Cash')
    ]
    payment = models.CharField(max_length=4, choices=PAYMENTS)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return f'Product ID: {self.pk}'
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_item')
    quantity = models.PositiveIntegerField(default=1)

