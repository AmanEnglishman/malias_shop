from django.urls import path

from .views import ProfileListAPIView

urlpatterns = [
    path('profile-list/', ProfileListAPIView.as_view(), name='profile-list')
]
