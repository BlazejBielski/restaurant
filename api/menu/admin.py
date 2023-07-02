from django.contrib import admin

from menu import models

admin.site.register(models.Category)
admin.site.register(models.Dish)
admin.site.register(models.ProductImage)
