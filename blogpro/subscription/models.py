from django.db import models

# Create your models here.
class Product(models.Model):
    amount = models.IntegerField()
    order_id = models.CharField()
    status = models.BooleanField(default=False)