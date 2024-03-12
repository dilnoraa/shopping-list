from django.db import models
from datetime import datetime
from django_resized import ResizedImageField

class Product(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    created_at = models.DateTimeField(default=datetime.utcnow)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = ResizedImageField(size=[300, 300], upload_to='static/product_images/', blank=True, null=True, default=None)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ShoppingItem(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    created_at = models.DateTimeField(default=datetime.utcnow)
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    location = models.CharField(max_length=100, default=None)
    price = models.FloatField(blank=True, null=True, default=None)
    amount = models.IntegerField(blank=True, null=True, default=1)

    def __str__(self):
        return str(self.id)
