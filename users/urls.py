from django.urls import path
from .views import MyProfileView

urlpatterns = [
    path('my-profile/', MyProfileView.as_view(), name='my-profile'),
]
