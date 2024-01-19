from django.shortcuts import render, redirect
from django.http import HttpResponse
from food_consuming.models import Food, Consume


def say_hello(request):
    return HttpResponse("Hello world")
