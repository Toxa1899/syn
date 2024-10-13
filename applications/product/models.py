from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Внешний ключ на таблицу Category",
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Salesman(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    products = models.ManyToManyField(
        Product, verbose_name="Внешний ключ на таблицу Product"
    )

    class Meta:
        verbose_name = "Продавец"
        verbose_name_plural = "Продавец"


class SalesmanAdditionally(models.Model):
    salesman = models.OneToOneField(
        Salesman,
        on_delete=models.CASCADE,
        verbose_name="Внешний ключ на таблицу Salesman",
    )
    description = models.TextField(verbose_name="описание")

    class Meta:
        verbose_name = "доп описание к продавцу"
        verbose_name_plural = "доп описание к продавцам"
