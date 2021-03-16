from rest_framework import generics, viewsets

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.generics import get_object_or_404

class CategorysAPIView(generics.ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = CategorySerializer

class CategoryAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Product.objects.all()
    serializer_class = CategorySerializer

class ProductsAPIView(generics.ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        
        if self.kwargs.get('category_pk'):

            return self.queryset.filter(category_id=self.kwargs.get('category_pk'))

        return self.queryset.all()

class ProductAPIView(generics.ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_object(self):
        
        if self.kwargs.get('category_pk'):

            return get_object_or_404(self.get_queryset(), category_id=self.kwargs.get('category_pk'), pk=self.kwargs.get('product_pk'))

        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('product_pk'))

class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=True, methods=['get'])
    def products(self, response, pk=None):

        self.pagination_class.page_size = 1
        
        products = Product.objects.filter(category_id=pk)

        page = self.paginate_queryset(products)

        if page is not None:

            serializer = ProductSerializer(page, many=True)

            return self.get_paginated_response(serializer.data)

        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)

class ProductViewSet(
                        mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet
                    ):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer