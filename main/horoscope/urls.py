from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:sign_zodiac>', views.get_info_about_num),
    path('<str:sign_zodiac>', views.get_info_about, name="horoscope-name"),
]