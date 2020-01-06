from django.db import models


class productData(models.Model):
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=100)
    product_cost = models.IntegerField()
    product_class = models.CharField(max_length=20)
    no_of_product = models.IntegerField()
    manufacture_date = models.DateField(max_length=100)
    expiry_date = models.DateField(max_length=1000)
    customer_name = models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    email = models.EmailField(max_length=100)