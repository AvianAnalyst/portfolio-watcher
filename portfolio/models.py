from django.db import models
from datetime import date


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Investment(models.Model):
    cost = models.FloatField()
    num_of_shares = models.IntegerField()
    purchase_date = models.DateField(default=date.today)
    entry_date = models.DateField(auto_now=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)




