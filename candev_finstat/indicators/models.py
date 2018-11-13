from django.db import models


class ConsumerPriceIndex(models.Model):
    date = models.DateField()
    all_fields = models.DecimalField(max_digits=5, decimal_places=2)
    food = models.DecimalField(max_digits=5, decimal_places=2)
    shelter = models.DecimalField(max_digits=5, decimal_places=2)
    transportation = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.date} - ({self.all_fields}, {self.food}, {self.shelter}, {self.transportation})"
