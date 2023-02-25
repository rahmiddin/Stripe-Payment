from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=250, verbose_name='Описание')
    price = models.PositiveIntegerField(verbose_name='Цена')

    def __str__(self):
        return self.name