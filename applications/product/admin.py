from django.contrib import admin

from applications.product.models import (
    Category,
    Product,
    Salesman,
    SalesmanAdditionally,
)

# Register your models here.
admin.site.register(Salesman)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(SalesmanAdditionally)
