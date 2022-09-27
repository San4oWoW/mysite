from django.urls import path, include
from . import views

urlpatterns = [
    path('<sign_zodiac>/', views.get_info_about),
]