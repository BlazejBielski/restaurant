from . import viewsets
from rest_framework.routers import DefaultRouter

app_name = 'menu'

router = DefaultRouter()
router.register(r'categories', viewsets.CategoryViewSet, basename='category-view-set')
router.register(r'dishes', viewsets.DishViewSet, basename='dish-view-set')

urlpatterns = [
    *router.urls
]
