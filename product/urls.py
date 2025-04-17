from django.urls import path
from .views import CategoryWithProductsListView

urlpatterns = [
    path('', CategoryWithProductsListView.as_view(), name='category-list'),
]
