from django.db import models

# Create your models here.
class Car(models.Model):
    MECHANIC, AUTO, ROBOT = range(3)
    KPP_CHOICES = [
        [MECHANIC, "Механическая коробка передач"],
        [AUTO, "Автоматическая коробка передач"],
        [ROBOT, "Роботизированная коробка передач"],
    ]
    manufacturer = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField()
    kpp = models.SmallIntegerField(choices=KPP_CHOICES)
    color = models.CharField(max_length=255)

    def __str__(self):
        return self.manufacturer