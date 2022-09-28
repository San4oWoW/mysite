from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

zodiac_dict = {
    "aries": '21.03-20.04',
    "taurus": '21.04-21.05',
    "gemini": '22.05-21.06',
    "cancer": '22.06-22.07',
    "lio": '23.07-22.08',
    "virgo": '23.08-23.09',
    "libra": '24.09-23.10',
    "scorpio": '24.10-22.11',
    "sagittarius": '23.11-21.12',
    "capricorn": '22.12-20.01',
    "aquarius": '21.01-18.02',
    "pisces": '19.02-20.03',
}


def get_info_about(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac, None)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f"Неизвестный знак зодиака - {sign_zodiac}")



def get_info_about_num(request, sign_zodiac: int):
    return HttpResponse(f"This number is {sign_zodiac}")

def test():
    pass