from django.db import models
from datetime import datetime,timedelta

class Customer(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(default='abc@gmail.com')

    def __str__(self):
        return self.name

class product(models.Model):
    name=models.CharField(max_length=100)
    descp=models.TextField()
    price=models.IntegerField()
    seller=models.ForeignKey('Customer',on_delete=models.CASCADE,related_name='products')
    product_active=models.BooleanField(default=True)
    date=models.DateTimeField(auto_now_add=True,null=True)

    def registered_date(self):
        two_month=datetime.now() - timedelta(days=60)
        return self.date <= two_month

    def __str__(self):
        return self.name