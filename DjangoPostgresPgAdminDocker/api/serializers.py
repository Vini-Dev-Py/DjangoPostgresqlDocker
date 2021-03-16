from rest_framework import serializers

from .models import Category, Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:

        model = Product

        fields = (
            'id',
            'name',
            'price',
            'category',
            'quantity',
            'criacao',
            'ativo'
        )

class CategorySerializer(serializers.ModelSerializer):

    products = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='product-detail'
    )

    class Meta:

        extra_kwargs = {
            'name': {
                'write_only': True
            }
        }

        model = Category

        fields = (
            'id',
            'name',
            'criacao',
            'ativo',
            'products'
        )