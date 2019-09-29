from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200, blank=False, null=True)
    product_description = models.TextField(max_length=500, blank=True, null=True)
    product_price = models.DecimalField(max_digits=100000, decimal_places=2, blank=False, null=True)

    def __str__(self):
        return self.product_name