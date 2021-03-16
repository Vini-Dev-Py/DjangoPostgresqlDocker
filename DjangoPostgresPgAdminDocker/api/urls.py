from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (
    CategoryAPIView,
    CategorysAPIView,
    ProductAPIView,
    ProductsAPIView,
    CategoryViewSet,
    ProductViewSet
)

router = SimpleRouter()
router.register('categorys', CategoryViewSet)
router.register('products', ProductViewSet)

urlpatterns = [
    path('categorys/', CategorysAPIView.as_view(), name='categorys'),
    path('categorys/<int:pk>/', CategoryAPIView.as_view(), name='category'),
    path('categorys/<int:category_pk>/products/', ProductsAPIView.as_view(), name='category_products'),
    path('categorys/<int:categorys_pk>/products/<int:product_pk>/', ProductAPIView.as_view(), name='category_product'), #
    path('products/', ProductsAPIView.as_view(), name='products'),
    path('products/<int:product_pk>/', ProductAPIView.as_view(), name='product')
]