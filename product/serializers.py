from rest_framework import serializers
from .models import Category, Product, Review


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


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Review
        fields =('id', 'product', 'user', 'rating', 'created_at')
        read_only_fields = ['created_at']
        validators = []  # <-- отключает проверку unique_together от DRF


    def create(self, validated_data):
        user = validated_data['user']
        product = validated_data['product']
        rating = validated_data['rating']

        # Ищем уже существующий отзыв
        existing = Review.objects.filter(user=user, product=product).first()
        if existing:
            # Обновляем и возвращаем
            existing.rating = rating
            existing.save()
            return existing

        # Если нет — создаём
        return super().create(validated_data)