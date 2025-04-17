from django.urls import path
from .views import CategoryWithProductsListView, ReviewCreateView

urlpatterns = [
    path('', CategoryWithProductsListView.as_view(), name='category-list'),
    path('reviews/', ReviewCreateView.as_view(), name='review-create'),
]
