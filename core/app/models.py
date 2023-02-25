from django.db import models


class Item(models.Model):
    name = models.CharField(verbose_name='Название', max_length=100, null=False, blank=False)
    description = models.TextField(verbose_name='Описание', max_length=2000, null=True, blank=True)
    price = models.IntegerField(verbose_name='Цена', null=False, blank=False)

    def __str__(self):
        return f'{self.name} - {self.price}'


class Order(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.item}'
