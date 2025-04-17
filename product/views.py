from rest_framework import generics
from .models import Category
from .serializers import CategoryWithProductsSerializer


class CategoryWithProductsListView(generics.ListAPIView):
    queryset = Category.objects.filter(parent=None)
    serializer_class = CategoryWithProductsSerializer
