from django.urls import path
from accounts.views import UserCreateView




urlpatterns = [
    path('users/', UserCreateView.as_view(), name='user-create'),
]