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
    name = models.CharField(max_length=50)
    products = models.ManyToManyField(Product)


class SalesmanAdditionally(models.Model):
    salesman = models.OneToOneField(Salesman, on_delete=models.CASCADE)
    description = models.TextField()
