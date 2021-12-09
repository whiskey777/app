from types import BuiltinMethodType
from django.db import models

# Create your models here.
class Metal(models.Model):
    date = models.DateField()
    code = models.IntegerField ()
    name = models.CharField(max_length=100)
    buy = models.CharField(max_length=7)
    sell = models.CharField(max_length=7)
