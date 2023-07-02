from django.db import models
from utilities.timestamp_model import TimeStampModel


class ProductImage(models.Model):
    image = models.ImageField(upload_to="product_image")
    product = models.ForeignKey("Dish", on_delete=models.CASCADE, related_name="images")


class Category(TimeStampModel):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return str(self.name)


class Dish(TimeStampModel):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey("Category", on_delete=models.DO_NOTHING, related_name="categories")

    def __str__(self):
        return str(self.name)
