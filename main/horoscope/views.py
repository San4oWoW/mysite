from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.


def get_info_about(request, sign_zodiac):
    if sign_zodiac == "leo":
        return HttpResponse("Знак зодиака лев")
    elif sign_zodiac == "scorpio":
        return HttpResponse("Знак зодиака скорпион")
    else:
        return HttpResponseNotFound(f"Неизвестный знак зодиака - {sign_zodiac}")
