from django.db import models

class bitcoinprice(models.Model):
    date = models.DateField()
    price =models.DecimalField()
    exchange =models.IntegerField()
