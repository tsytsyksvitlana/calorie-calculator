from django.urls import path
from food_consuming import views

urlpatterns = [
    path('hello/', views.say_hello, name="hello")
]
