from django.urls import path
from . import views

urlpatterns = [
    path('', views.apod_page, name="apod_page"),
]
