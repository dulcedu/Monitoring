from django.db import models

class bitcoinprice(models.Model):
    date = models.DateField()
    price =models.DecimalField(max_digits=10, decimal_places=2)
    exchange =models.IntegerField()
