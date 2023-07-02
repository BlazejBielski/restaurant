from rest_framework import serializers

from . import models


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = ('name',)


class DishSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Dish
        fields = ('name', 'description', 'price', 'category', 'images')
