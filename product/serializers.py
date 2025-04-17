from rest_framework import serializers
from .models import Category, Product


class ProductSerializer(serializers.ModelSerializer):
    average_rating = serializers.FloatField(read_only=True)

    class Meta:
        model = Product
        fields = (
            'id', 'title', 'image', 'price', 'discount', 'discount_amount',
            'created_at', 'average_rating', 'is_new', 'average_rating'
        )


class RecursiveCategorySerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = CategoryWithProductsSerializer(value, context=self.context)
        return serializer.data


class CategoryWithProductsSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    children = RecursiveCategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'products', 'children']

    def get_products(self, obj):
        products = obj.product_set.all()
        return ProductSerializer(products, many=True).data
