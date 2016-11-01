from __future__ import unicode_literals
from django.db import models


class Parts(models.Model):
    code_text = models.CharField(max_length=50)
    name_text = models.CharField(max_length=50)
    brand_text = models.CharField(max_length=50)
    number_stock = models.CharField(max_length=50)
    number_reserve = models.CharField(max_length=50)
    price_float = models.FloatField()
    price_discount = models.FloatField()
    note_text = models.CharField(max_length=50)
