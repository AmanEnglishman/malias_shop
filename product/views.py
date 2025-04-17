from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category
from .serializers import CategoryWithProductsSerializer, ReviewSerializer


class CategoryWithProductsListView(generics.ListAPIView):
    queryset = Category.objects.filter(parent=None)
    serializer_class = CategoryWithProductsSerializer


class ReviewCreateView(APIView):

    def post(self, request):
        serializer = ReviewSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            review = serializer.save()
            return Response(ReviewSerializer(review).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
